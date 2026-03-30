from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Studio Backend Running 🚀"}

@app.get("/test")
def test():
    return {"status": "working"}
