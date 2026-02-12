from fastapi import FastAPI
from .db import SessionLocal
from .models import Player
from .init_db import init

app = FastAPI(title="Chatbot Sword Game API")

init()

@app.get("/status")
def status():
    db = SessionLocal()
    player = db.query(Player).first()
    result = {
        "gold": player.gold,
        "weapon_level": player.weapon_level
    }
    db.close()
    return result