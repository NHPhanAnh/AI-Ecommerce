from fastapi import FastAPI
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

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = ai_engine.ask(request.query)
    return ChatResponse(response=answer)
