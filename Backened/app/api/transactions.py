from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_transactions
from app.schemas import ProductTransaction
from typing import List

router = APIRouter()

@router.get("/transactions", response_model=List[ProductTransaction])
def read_transactions(skip: int = 0, limit: int = 10, search: str = None, db: Session = Depends(get_db)):
    transactions = get_transactions(db, skip=skip, limit=limit, search=search)
    return transactions
