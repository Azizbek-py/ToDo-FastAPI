from fastapi import FastAPI
from routes import todo_router, index_router
from database.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)
app.include_router(index_router)
