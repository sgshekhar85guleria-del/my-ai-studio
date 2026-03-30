from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root API
@app.get("/")
def home():
    return {"message": "AI Studio Backend Running 🚀"}

# Test API
@app.get("/test")
def test():
    return {"status": "working"}

# Chat Request Model
class ChatRequest(BaseModel):
    message: str

# Chat API
@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    # Dummy AI response (abhi basic hai)
    return {
        "reply": f"You said: {user_message}"
    }
