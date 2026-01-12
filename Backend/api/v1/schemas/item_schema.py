from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    invoice_id: int
    description: str
    quantity: int
    rate: float
    tax_percent: float
    amount: float

class ItemResponse(BaseModel):
    id: int
    invoice_id: int
    description: str
    quantity: int
    rate: float
    tax_percent: float
    amount: float

    class Config:
        from_attributes = True
