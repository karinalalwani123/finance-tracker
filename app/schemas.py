from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# -------- USER --------
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    role: str = "viewer"

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True


# -------- TRANSACTION --------
class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0)  # must be > 0
    type: str
    category: str
    date: date
    notes: Optional[str] = None


class TransactionCreate(TransactionBase):
    user_id: int


class TransactionUpdate(BaseModel):
    amount: Optional[float]
    type: Optional[str]
    category: Optional[str]
    date: Optional[date]
    notes: Optional[str]


class TransactionResponse(TransactionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float