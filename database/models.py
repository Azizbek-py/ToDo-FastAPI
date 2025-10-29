from sqlalchemy import Column, Integer, String
from .config import Base

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description  = Column(String, nullable=True)