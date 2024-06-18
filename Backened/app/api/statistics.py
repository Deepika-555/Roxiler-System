from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_statistics

router = APIRouter()

@router.get("/statistics")
def read_statistics(month: int, db: Session = Depends(get_db)):
    return get_statistics(db, month=month)
