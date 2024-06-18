from pydantic import BaseModel
from datetime import date

class ProductTransactionBase(BaseModel):
    title: str
    description: str
    price: float
    sold: bool
    dateOfSale: date
    category: str

class ProductTransactionCreate(ProductTransactionBase):
    pass

class ProductTransaction(ProductTransactionBase):
    id: int

    class Config:
        orm_mode = True
