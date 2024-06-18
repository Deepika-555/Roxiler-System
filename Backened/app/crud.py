from sqlalchemy.orm import Session
from app.models import ProductTransaction
from app.schemas import ProductTransactionCreate
from sqlalchemy import func, extract

def create_transaction(db: Session, transaction: ProductTransactionCreate):
    db_transaction = ProductTransaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, skip: int = 0, limit: int = 10, search: str = None):
    query = db.query(ProductTransaction)
    if search:
        query = query.filter(
            (ProductTransaction.title.contains(search)) |
            (ProductTransaction.description.contains(search)) |
            (ProductTransaction.price == float(search))
        )
    return query.offset(skip).limit(limit).all()

def get_statistics(db: Session, month: int):
    total_sales = db.query(func.sum(ProductTransaction.price)).filter(
        extract('month', ProductTransaction.dateOfSale) == month,
        ProductTransaction.sold == True
    ).scalar()
    
    total_sold_items = db.query(func.count(ProductTransaction.id)).filter(
        extract('month', ProductTransaction.dateOfSale) == month,
        ProductTransaction.sold == True
    ).scalar()
    
    total_not_sold_items = db.query(func.count(ProductTransaction.id)).filter(
        extract('month', ProductTransaction.dateOfSale) == month,
        ProductTransaction.sold == False
    ).scalar()

    return {
        "total_sales": total_sales,
        "total_sold_items": total_sold_items,
        "total_not_sold_items": total_not_sold_items
    }

def get_barchart_data(db: Session, month: int):
    price_ranges = [
        (0, 100), (101, 200), (201, 300), (301, 400),
        (401, 500), (501, 600), (601, 700), (701, 800),
        (801, 900), (901, float('inf'))
    ]
    barchart_data = []
    for lower, upper in price_ranges:
        count = db.query(func.count(ProductTransaction.id)).filter(
            extract('month', ProductTransaction.dateOfSale) == month,
            ProductTransaction.price.between(lower, upper)
        ).scalar()
        barchart_data.append({"range": f"{lower}-{upper}", "count": count})
    return barchart_data

def get_piechart_data(db: Session, month: int):
    categories = db.query(
        ProductTransaction.category, func.count(ProductTransaction.id)
    ).filter(
        extract('month', ProductTransaction.dateOfSale) == month
    ).group_by(ProductTransaction.category).all()
    return [{"category": category, "count": count} for category, count in categories]
