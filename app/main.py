from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import transactions, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "Finance Tracker API Running 🚀"}