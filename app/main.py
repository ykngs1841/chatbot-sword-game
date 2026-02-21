import random
from fastapi import HTTPException
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

def get_success_rate(level: int) -> float:
    if level <= 3:
        return 0.8
    elif level <= 6:
        return 0.5
    else:
        return 0.2
    
@app.post("/upgrade")
def upgrade():
    db = SessionLocal()
    player = db.query(Player).first()

    before_level = player.weapon_level
    cost = 100 * player.weapon_level

    if player.gold < cost:
        db.close()
        raise HTTPException(status_code=400, detail="골드 부족")

    player.gold -= cost

    success_rate = get_success_rate(player.weapon_level)
    success_rate += player.fail_stack * 0.05  # 🔥 실패 누적 보정

    if random.random() < success_rate:
        player.weapon_level += 1
        player.fail_stack = 0
        result = "success"
    else:
        player.weapon_level = max(1, player.weapon_level - 1)  # 패널티
        player.fail_stack += 1
        result = "fail"

    # 로그 저장
    log = UpgradeLog(
        result=result,
        before_level=before_level,
        after_level=player.weapon_level
    )
    db.add(log)

    db.commit()

    gold = player.gold
    weapon_level = player.weapon_level
    fail_stack = player.fail_stack

    db.close()

    return {
        "result": result,
        "gold": gold,
        "weapon_level": weapon_level,
        "fail_stack": fail_stack,
        "success_rate": round(success_rate, 2)
    }