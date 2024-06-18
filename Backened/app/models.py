from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from app.database import Base

class ProductTransaction(Base):
    __tablename__ = "product_transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    sold = Column(Boolean)
    dateOfSale = Column(Date)
    category = Column(String, index=True)
