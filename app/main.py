from fastapi import FastAPI

app = FastAPI(title="Chatbot Sword Game API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/status")
def status():
    return {
        "gold": 1000,
        "weapon_level": 1
    }
