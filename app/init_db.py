from .db import engine, SessionLocal
from .models import Player, Base

def init():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if not db.query(Player).first():
        db.add(Player())
        db.commit()
    db.close()