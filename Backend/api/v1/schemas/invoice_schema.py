from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from .item_schema import ItemResponse

class InvoiceCreate(BaseModel):
    vendor_id: int
    invoice_number: str
    invoice_date: Optional[date]
    subtotal: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    currency: Optional[str] = "INR"

class InvoiceUpdate(BaseModel):
    vendor_id: Optional[int]
    invoice_number: Optional[str]
    invoice_date: Optional[date]
    subtotal: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    currency: Optional[str]

class InvoiceResponse(BaseModel):
    id: int
    vendor_id: int
    invoice_number: str
    invoice_date: Optional[date]
    subtotal: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    currency: Optional[str]
    items: List[ItemResponse] = []

    class Config:
        from_attributes = True
