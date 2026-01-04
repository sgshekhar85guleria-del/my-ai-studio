from fastapi import FastAPI
from schemas import PromptRequest
from config import AI_MODE
from ai_runner.mock import MockAIRunner

app = FastAPI(title="Agency AI Backend")

def get_ai_runner():
    if AI_MODE == "mock":
        return MockAIRunner()
    else:
        raise NotImplementedError("Real AI runner not implemented yet")

@app.post("/generate/text")
def generate_text(data: PromptRequest):
    ai = get_ai_runner()
    return ai.generate_text(data.prompt)

@app.post("/generate/image")
def generate_image(data: PromptRequest):
    ai = get_ai_runner()
    return ai.generate_image(data.prompt)

@app.post("/generate/video")
def generate_video(data: PromptRequest):
    ai = get_ai_runner()
    return ai.generate_video(data.prompt)
