import os
import requests
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma

# Thiết lập URL nội mạng của Docker
PRODUCT_API = os.environ.get("PRODUCT_SERVICE_URL", "http://product-service:8002/products/")

class AIEngine:
    def __init__(self):
        self.google_api_key = os.environ.get("GOOGLE_API_KEY")
        if not self.google_api_key:
            print("WARNING: GOOGLE_API_KEY is missing!")

        # Model Embeddings (Chuyển hoá text thành các Vector toán học)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        # Model LLM để đàm thoại
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
        self.vector_store = None

    def initialize_kb(self):
        print(f"Fetching Products from {PRODUCT_API}")
        products = []
        try:
            r = requests.get(PRODUCT_API, timeout=10)
            if r.status_code == 200:
                products = r.json()
        except Exception as e:
            print(f"Error fetching products: {e}")

        docs = []
        for item in products:
            cat = item.get('category', 'Khác')
            content = f"Tên Sản Phẩm: {item.get('name')}. Danh mục: {cat}. Giá Phân Phối: {item.get('price')}$. Tồn kho: {item.get('stock')} chiếc. Đang giảm giá: {item.get('discount_percent')}%. Thông số chi tiết: {item.get('description', '')}"
            metadata = {"source": "product-service", "id": item.get("id"), "category": cat}
            docs.append(Document(page_content=content, metadata=metadata))

        if docs:
            print(f"Bắt đầu nhúng (embed) và lưu trữ {len(docs)} mẩu dữ liệu vào VectorDB Chroma...")
            self.vector_store = Chroma.from_documents(docs, self.embeddings, persist_directory="./chroma_db_store")
            print("Khởi tạo VectorDB thành công!")
        else:
            print("CRITICAL WARNING: Không có tài liệu mẫu nào được nạp lên.")

    def ask(self, query: str, history: list = None) -> str:
        if not self.vector_store:
            return "❌ Hệ thống tri thức nội bộ chưa được tải dữ liệu, vui lòng báo quản trị viên."
        
        hist_text = ""
        if history:
            for msg in history:
                role = "USER" if msg.role == "user" else "AI"
                hist_text += f"{role}: {msg.text}\n"

        # Thiết lập mô hình tìm kiếm Top 3 thông tin giống nhất
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        
        # Template RAG (Nhồi kiến thức vào ngữ cảnh LLM)
        prompt = PromptTemplate.from_template(
            "Bạn là trợ lý AI ảo nhiệt tình và rất chuyên nghiệp của hệ thống bán hàng 'Tech Store'.\n"
            "Hãy sử dụng thông tin KHO HÀNG để trả lời rành mạch. Nếu câu hỏi liên quan đến nội dung cũ, hãy dựa vào LỊCH SỬ CHUYỆN TRÒ để hiểu ngữ cảnh (Ví dụ người dùng nói 'Tôi mua nó', bạn phải tự truy vết 'nó' là món nào ở trên).\n\n"
            "--- LỊCH SỬ CHUYỆN TRÒ: ---\n{hist_text}\n"
            "--- THÔNG TIN KHO HÀNG (NGỮ CẢNH): ---\n{context}\n\n"
            "CÂU HỎI MỚI CỦA KHÁCH HÀNG: {input}\n\n"
            "TRẢ LỜI CỦA BẠN:"
        )
        
        document_chain = create_stuff_documents_chain(self.llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        try:
            response = retrieval_chain.invoke({"input": query, "hist_text": hist_text})
            return response["answer"]
        except Exception as e:
            return f"❌ Lỗi khi giao tiếp cùng AI Kernel: {str(e)}"
