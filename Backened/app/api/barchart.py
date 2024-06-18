from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_barchart_data

router = APIRouter()

@router.get("/barchart")
def read_barchart(month: int, db: Session = Depends(get_db)):
    return get_barchart_data(db, month=month)
