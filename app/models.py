from sqlalchemy import Column, Integer
from .db import Base
from sqlalchemy import String

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    gold = Column(Integer, default=1000)
    weapon_level = Column(Integer, default=1)
    fail_stack = Column(Integer, default=0)

class UpgradeLog(Base):
    __tablename__ = "upgrade_logs"

    id = Column(Integer, primary_key=True, index=True)
    result = Column(String)
    before_level = Column(Integer)
    after_level = Column(Integer)