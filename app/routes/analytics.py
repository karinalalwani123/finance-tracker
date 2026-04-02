from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import SessionLocal
from .. import models
from ..schemas import SummaryResponse

router = APIRouter()


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- SUMMARY --------
@router.get("/analytics/summary", response_model=SummaryResponse)
def get_summary(db: Session = Depends(get_db)):
    
    total_income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "income"
    ).scalar()

    total_expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "expense"
    ).scalar()

    total_income = total_income or 0
    total_expense = total_expense or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }