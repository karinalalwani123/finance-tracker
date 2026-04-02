from sqlalchemy.orm import Session
from . import models, schemas


# -------- CREATE TRANSACTION --------
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


# -------- GET ALL TRANSACTIONS --------
def get_transactions(db: Session):
    return db.query(models.Transaction).all()


# -------- GET SINGLE TRANSACTION --------
def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()


# -------- UPDATE TRANSACTION --------
def update_transaction(db: Session, transaction_id: int, updated_data: schemas.TransactionUpdate):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction


# -------- DELETE TRANSACTION --------
def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return transaction