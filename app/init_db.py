from .db import engine, SessionLocal
from .models import Player, Base

def init():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(Player).first():
        player = Player(gold=100, weapon_level=1, fail_stack=0)
        db.add(Player())
        db.commit()
    db.close()