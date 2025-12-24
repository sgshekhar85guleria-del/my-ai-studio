from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Agency AI Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/generate")
def generate(data: Prompt):
    return {
        "message": "Prompt received",
        "prompt": data.prompt
    }
