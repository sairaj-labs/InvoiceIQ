from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from repositories.invoice_repository import InvoiceRepository
from repositories.item_repository import ItemRepository
from api.v1.schemas.invoice_schema import InvoiceCreate, InvoiceUpdate, InvoiceResponse
from api.v1.schemas.item_schema import ItemCreate, ItemResponse

router = APIRouter(tags=["Invoices"])

@router.post("/", response_model=InvoiceResponse)
def create_invoice(payload: InvoiceCreate, db: Session = Depends(get_db)):
    invoice = InvoiceRepository.create(db, payload.dict())
    return invoice

@router.get("/", response_model=list[InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    return InvoiceRepository.get_all(db)

@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = InvoiceRepository.get_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.put("/{invoice_id}", response_model=InvoiceResponse)
def update_invoice(invoice_id: int, payload: InvoiceUpdate, db: Session = Depends(get_db)):
    invoice = InvoiceRepository.get_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(invoice, field, value)

    db.commit()
    db.refresh(invoice)
    return invoice

@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    deleted = InvoiceRepository.delete(db, invoice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted successfully"}
