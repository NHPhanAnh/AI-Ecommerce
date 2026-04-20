import os
import random
import requests
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from lstm_recommender import LSTMRecommender
    LSTM_AVAILABLE = True
except Exception as e:
    print(f"[engine] LSTM import failed: {e}")
    LSTM_AVAILABLE = False

# ------------------------------------------------------------------ #
#  Fallback Embeddings khi Google API lỗi                             #
# ------------------------------------------------------------------ #
class DummyEmbeddings:
    """Embeddings giả để VectorDB vẫn khởi tạo được khi API Key lỗi."""
    def embed_documents(self, texts):
        return [[round(random.uniform(-0.1, 0.1), 4)] * 768 for _ in texts]
    def embed_query(self, text):
        return [round(random.uniform(-0.1, 0.1), 4)] * 768

# ------------------------------------------------------------------ #
#  Config                                                              #
# ------------------------------------------------------------------ #
PRODUCT_API = os.environ.get("PRODUCT_SERVICE_URL", "http://product-service:8002/products/")
MODEL_PATH  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_best.h5")


class AIEngine:
    def __init__(self):
        self.google_api_key = os.environ.get("GOOGLE_API_KEY")
        self.vector_store   = None
        self.llm            = None
        self.products       = []     # Cache sản phẩm thật từ product-service
        self.use_gemini     = False  # Cờ biết có dùng Google hay không

        # LSTM Recommender — load model đã train trên data_user500.csv
        self.recommender = None
        if LSTM_AVAILABLE:
            try:
                self.recommender = LSTMRecommender(
                    vocab_size=100,
                    embedding_dim=64,
                    max_sequence_len=5,
                    model_path=MODEL_PATH
                )
                print("[AIEngine] LSTM Recommender sẵn sàng!")
            except Exception as e:
                print(f"[AIEngine] LSTM init error: {e}")

        # Khởi tạo Gemini (nếu có Key)
        if self.google_api_key:
            try:
                self.embeddings = GoogleGenerativeAIEmbeddings(
                    model="models/gemini-embedding-001"
                )
                self.llm = ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash", temperature=0.3
                )
                self.use_gemini = True
                print("[AIEngine] Gemini API sẵn sàng!")
            except Exception as e:
                print(f"[AIEngine] Gemini init error: {e}")
        else:
            print("[AIEngine] WARNING: Không có GOOGLE_API_KEY — chạy chế độ LSTM-only.")

    # ------------------------------------------------------------------ #
    #  Nạp dữ liệu sản phẩm vào VectorDB                                 #
    # ------------------------------------------------------------------ #
    def initialize_kb(self):
        print(f"[AIEngine] Fetching products from {PRODUCT_API}")
        try:
            r = requests.get(PRODUCT_API, timeout=10)
            if r.status_code == 200:
                self.products = r.json()
                print(f"[AIEngine] Đã lấy {len(self.products)} sản phẩm.")
        except Exception as e:
            print(f"[AIEngine] Error fetching products: {e}")

        # Cập nhật danh sách sản phẩm cho LSTM Recommender
        if self.recommender is not None:
            self.recommender.products = self.products

        # Tạo Documents cho VectorDB
        docs = []
        for item in self.products:
            cat = item.get("category", "Khác")
            content = (
                f"Tên: {item.get('name')}. "
                f"Danh mục: {cat}. "
                f"Giá: {item.get('price')}đ. "
                f"Tồn kho: {item.get('stock')} chiếc. "
                f"Giảm giá: {item.get('discount_percent', 0)}%. "
                f"Mô tả: {item.get('description', '')}"
            )
            docs.append(Document(
                page_content=content,
                metadata={"id": item.get("id"), "name": item.get("name"), "category": cat}
            ))

        if not docs:
            print("[AIEngine] WARNING: Không có sản phẩm nào để nhúng.")
            return

        print(f"[AIEngine] Nhúng {len(docs)} sản phẩm vào VectorDB...")

        # Thử dùng Gemini Embeddings trước
        if self.use_gemini:
            try:
                self.vector_store = Chroma.from_documents(
                    docs, self.embeddings, persist_directory="./chroma_db_store"
                )
                print("[AIEngine] VectorDB (Gemini Embeddings) sẵn sàng!")
                return
            except Exception as e:
                print(f"[AIEngine] Gemini embedding lỗi: {e}")
                print("[AIEngine] Chuyển sang DummyEmbeddings + LSTM-only mode.")
                self.use_gemini = False
                self.llm = None

        # Fallback: DummyEmbeddings để VectorDB vẫn có dữ liệu sản phẩm
        try:
            self.vector_store = Chroma.from_documents(
                docs, DummyEmbeddings(), persist_directory="./chroma_mock_store"
            )
            print("[AIEngine] VectorDB (DummyEmbeddings) sẵn sàng — LSTM mode.")
        except Exception as e:
            print(f"[AIEngine] VectorDB fallback lỗi: {e}")

    # ------------------------------------------------------------------ #
    #  Trả lời chat                                                       #
    # ------------------------------------------------------------------ #
    def ask(self, query: str, history: list = None) -> str:
        if not self.vector_store and not self.products:
            return "❌ Hệ thống chưa tải được dữ liệu sản phẩm. Vui lòng thử lại sau."

        # ---- LSTM Recommendation ----
        lstm_text = ""
        q_lower = query.lower()
        lstm_keywords = ["đề xuất", "gợi ý", "mua gì", "giới thiệu",
                         "recommend", "nên mua", "phù hợp", "tầm giá"]
        if any(k in q_lower for k in lstm_keywords) and self.recommender:
            try:
                # Dùng session giả lập (trong thực tế lấy từ cookie/session user)
                dummy_session = [random.randint(1, 50) for _ in range(5)]
                lstm_text = self.recommender.get_recommendation_text(dummy_session)
            except Exception as e:
                lstm_text = f"\n\n🤖 [LSTM] Lỗi phân tích: {e}"

        # ---- Nếu Gemini hoạt động → RAG đầy đủ ----
        if self.use_gemini and self.llm and self.vector_store:
            return self._ask_with_rag(query, history, lstm_text)

        # ---- Fallback: Rule-based từ danh sách sản phẩm + LSTM ----
        return self._ask_rule_based(query, lstm_text)

    def _ask_with_rag(self, query: str, history: list, lstm_text: str) -> str:
        """Chat có RAG đầy đủ (dùng Gemini LLM + VectorDB)."""
        hist_text = ""
        if history:
            for msg in history:
                role = "USER" if msg.role == "user" else "AI"
                hist_text += f"{role}: {msg.text}\n"

        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        prompt = PromptTemplate.from_template(
            "Bạn là trợ lý AI nhiệt tình của cửa hàng công nghệ 'Tech Store'.\n"
            "Dùng thông tin KHO HÀNG để trả lời chính xác. "
            "Nếu câu hỏi cũ, dùng LỊCH SỬ để hiểu ngữ cảnh.\n\n"
            "--- LỊCH SỬ: ---\n{hist_text}\n"
            "--- KHO HÀNG: ---\n{context}\n\n"
            "CÂU HỎI: {input}\n\n"
            "TRẢ LỜI:"
        )
        doc_chain = create_stuff_documents_chain(self.llm, prompt)
        chain = create_retrieval_chain(retriever, doc_chain)
        try:
            resp = chain.invoke({"input": query, "hist_text": hist_text})
            return resp["answer"] + lstm_text
        except Exception as e:
            return f"❌ Lỗi Gemini: {e}" + lstm_text

    def _ask_rule_based(self, query: str, lstm_text: str) -> str:
        """
        Chat không cần Gemini — dùng keyword matching trên danh sách sản phẩm thật.
        Tự trả lời dựa trên dữ liệu sản phẩm có sẵn.
        """
        q = query.lower()
        matched = []

        # Tìm sản phẩm theo từ khóa trong câu hỏi
        for p in self.products:
            name = (p.get("name") or "").lower()
            cat  = (p.get("category") or "").lower()
            desc = (p.get("description") or "").lower()
            # So khớp từ trong query với tên/danh mục/mô tả sản phẩm
            words = [w for w in q.split() if len(w) > 2]
            if any(w in name or w in cat or w in desc for w in words):
                matched.append(p)

        # Lọc theo giá nếu có đề cập ngân sách
        price_limit = None
        price_words = {"triệu": 1_000_000, "tr": 1_000_000, "nghìn": 1_000, "k": 1_000}
        import re
        nums = re.findall(r"(\d+(?:[.,]\d+)?)\s*(triệu|tr|nghìn|k)?", q)
        for num_str, unit in nums:
            try:
                val = float(num_str.replace(",", "."))
                multiplier = price_words.get(unit, 1)
                price_limit = val * multiplier
                break
            except:
                pass

        if price_limit and not matched:
            matched = [p for p in self.products
                       if float(p.get("price", 0) or 0) <= price_limit]

        # Xây dựng câu trả lời
        if matched:
            lines = [f"🛒 Tôi tìm thấy **{len(matched)} sản phẩm** phù hợp:\n"]
            for p in matched[:5]:
                name     = p.get("name", "Sản phẩm")
                price    = p.get("price", "N/A")
                discount = p.get("discount_percent", 0) or 0
                stock    = p.get("stock", 0)
                line = f"• **{name}** — {price}đ"
                if discount:
                    line += f" *(Giảm {discount}%)*"
                if stock <= 5:
                    line += " ⚠️ Sắp hết hàng!"
                lines.append(line)
            if len(matched) > 5:
                lines.append(f"_(và {len(matched)-5} sản phẩm khác...)_")
            response = "\n".join(lines)
        else:
            # Gợi ý chung
            response = (
                "Xin chào! Tôi là trợ lý AI của **Tech Store** 🛍️\n\n"
                f"Chúng tôi có **{len(self.products)} sản phẩm** đa dạng. "
                "Bạn có thể hỏi về:\n"
                "• Laptop, điện thoại, máy tính bảng\n"
                "• Sản phẩm theo ngân sách (ví dụ: *laptop dưới 15 triệu*)\n"
                "• Sản phẩm đang giảm giá\n"
                "• Hoặc gõ **đề xuất** để xem gợi ý AI!"
            )

        return response + lstm_text
