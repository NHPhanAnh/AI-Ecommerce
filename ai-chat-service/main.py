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

@app.post("/api/refresh_kb")
async def refresh_kb(background_tasks: BackgroundTasks):
    background_tasks.add_task(ai_engine.initialize_kb)
    return {"message": "Knowledge base refresh triggered in background"}
