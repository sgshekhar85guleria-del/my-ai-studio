from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import time

from config import AI_MODE
from schemas import PromptRequest

from ai_runner.mock import MockAIRunner
from ai_runner.real import RealAIRunner

from memory.memory_manager import MemoryManager
from core.supreme_core import SupremeCore
from core.security_layer import SecurityLayer


app = FastAPI()

memory = MemoryManager()
security = SecurityLayer()


def get_runner():
    if AI_MODE == "real":
        print("🔥 USING REAL AI (OLLAMA)")
        return RealAIRunner()
    else:
        print("⚠️ USING MOCK AI")
        return MockAIRunner()


runner = get_runner()
core = SupremeCore(runner, memory, security)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🟢 MAIN AI ROUTE
@app.post("/generate/stream")
def generate_stream(req: PromptRequest):

    result = core.process(req.prompt)

    def stream():
        words = result.split(" ")
        for w in words:
            yield w + " "
            time.sleep(0.02)

    return StreamingResponse(stream(), media_type="text/plain")


# 🟢 CLEAR MEMORY
@app.post("/memory/clear")
def clear_memory():
    memory.clear()
    return {"status": "memory cleared"}


# 🟢 GET MEMORY (FOR DASHBOARD)
@app.get("/memory")
def get_memory():
    return memory.messages


# 🟢 GET SYSTEM LOGS (FOR DASHBOARD)
@app.get("/logs")
def get_logs():
    return core.system.get_logs()