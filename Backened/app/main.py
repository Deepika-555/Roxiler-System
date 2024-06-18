from fastapi import FastAPI
from app.database import engine, Base
from app.api import transactions, statistics, barchart, piechart, combined

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions.router, prefix="/api")
app.include_router(statistics.router, prefix="/api")
app.include_router(barchart.router, prefix="/api")
app.include_router(piechart.router, prefix="/api")
app.include_router(combined.router, prefix="/api")

# Add the initialization endpoint here
import requests
from fastapi import FastAPI, HTTPException
from app.database import engine, SessionLocal, Base
from app.models import ProductTransaction
from app.crud import create_transaction
from app.schemas import ProductTransactionCreate
from sqlalchemy.orm import Session
import datetime

THIRD_PARTY_API_URL = "https://s3.amazonaws.com/roxiler.com/product_transaction.json"

@app.get("/initialize")
async def initialize_database():
    response = requests.get(THIRD_PARTY_API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch data from third-party API")

    data = response.json()
    
    db: Session = SessionLocal()
    try:
        for item in data:
            item['dateOfSale'] = datetime.datetime.strptime(item['dateOfSale'], '%Y-%m-%d')
            transaction = ProductTransactionCreate(**item)
            create_transaction(db=db, transaction=transaction)
    finally:
        db.close()
    
    return {"status": "Database initialized successfully"}

