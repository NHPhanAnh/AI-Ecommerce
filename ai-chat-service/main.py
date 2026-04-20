from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from contextlib import asynccontextmanager

from engine import AIEngine

ai_engine = AIEngine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Khởi chạy nạp và Embeddings dữ liệu khi khởi động
    print("Initialize AI Engine...")
    ai_engine.initialize_kb()
    yield
    print("Shutting down AI Engine...")

app = FastAPI(lifespan=lifespan)

# Cho phép UI Web Customer gọi API qua AJAX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    text: str

class ChatRequest(BaseModel):
    query: str
    history: list[ChatMessage] = []

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = ai_engine.ask(request.query, request.history)
    return ChatResponse(response=answer)

@app.get("/api/recommend")
async def recommend(user_id: str = "anonymous", top_k: int = 3):
    """Trả về gợi ý sản phẩm từ mô hình LSTM (dùng khi user click/tìm kiếm)."""
    import random
    if ai_engine.recommender is None:
        return {"user_id": user_id, "recommendations": [], "model": "unavailable"}
    session = [random.randint(1, 50) for _ in range(5)]  # TODO: thay bằng session thật
    products = ai_engine.recommender.recommend_products(session, top_k=top_k)
    action_pred = ai_engine.recommender.predict_next_action(session)
    return {
        "user_id":         user_id,
        "predicted_action": action_pred["predicted_action"],
        "confidence":       round(action_pred["confidence"], 4),
        "recommendations":  [
            {"id": p.get("id"), "name": p.get("name"),
             "price": p.get("price"), "discount": p.get("discount_percent", 0)}
            for p in products
        ],
        "model": "LSTM-5-layer-trained-data_user500"
    }

@app.get("/api/products")
async def get_products():
    """Trả về danh sách sản phẩm cache trong AI service."""
    return {"count": len(ai_engine.products), "products": ai_engine.products}

@app.post("/api/refresh_kb")
async def refresh_kb(background_tasks: BackgroundTasks):
    background_tasks.add_task(ai_engine.initialize_kb)
    return {"message": "Knowledge base refresh triggered in background"}
