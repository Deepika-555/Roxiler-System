from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_piechart_data

router = APIRouter()

@router.get("/piechart")
def read_piechart(month: int, db: Session = Depends(get_db)):
    return get_piechart_data(db, month=month)
