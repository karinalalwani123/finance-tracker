from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal
from .. import models

router = APIRouter()


# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- CREATE --------
@router.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate,
    role: str = "admin",  # simulate role
    db: Session = Depends(get_db)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")

    return crud.create_transaction(db, transaction)


# -------- READ ALL --------
from typing import Optional
from datetime import date

@router.get("/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(
    transaction_type: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Transaction)
    
    if transaction_type:
        query = query.filter(models.Transaction.type == transaction_type)

    if category:
        query = query.filter(models.Transaction.category == category)

    if start_date:
        query = query.filter(models.Transaction.date >= start_date)

    if end_date:
        query = query.filter(models.Transaction.date <= end_date)

    return query.all()


# -------- READ ONE --------
@router.get("/transactions/{transaction_id}", response_model=schemas.TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.get_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


# -------- UPDATE --------
@router.put("/transactions/{transaction_id}", response_model=schemas.TransactionResponse)
def update_transaction(transaction_id: int, updated_data: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    transaction = crud.update_transaction(db, transaction_id, updated_data)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


# -------- DELETE --------
@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.delete_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted successfully"}