from sqlalchemy import Column, Integer
from .db import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    gold = Column(Integer, default=1000)
    weapon_level = Column(Integer, default=1)