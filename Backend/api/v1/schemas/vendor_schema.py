from pydantic import BaseModel
from typing import Optional

class VendorCreate(BaseModel):
    name: str
    gstin: Optional[str] = None
    address: Optional[str] = None

class VendorUpdate(BaseModel):
    name: Optional[str] = None
    gstin: Optional[str] = None
    address: Optional[str] = None

class VendorResponse(BaseModel):
    id: int
    name: str
    gstin: Optional[str]
    address: Optional[str]

    class Config:
        from_attributes = True
