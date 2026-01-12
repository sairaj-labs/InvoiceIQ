from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from repositories.vendor_repository import VendorRepository
from api.v1.schemas.vendor_schema import VendorCreate, VendorResponse, VendorUpdate

router = APIRouter(tags=["Vendors"])

@router.post("/", response_model=VendorResponse)
def create_vendor(payload: VendorCreate, db: Session = Depends(get_db)):
    vendor = VendorRepository.create(db, payload.name, payload.gstin, payload.address)
    return vendor

@router.get("/", response_model=list[VendorResponse])
def get_vendors(db: Session = Depends(get_db)):
    return VendorRepository.get_all(db)

@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = VendorRepository.get_by_id(db, vendor_id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

@router.put("/{vendor_id}", response_model=VendorResponse)
def update_vendor(vendor_id: int, payload: VendorUpdate, db: Session = Depends(get_db)):
    vendor = VendorRepository.get_by_id(db, vendor_id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    if payload.name is not None:
        vendor.name = payload.name
    if payload.gstin is not None:
        vendor.gstin = payload.gstin
    if payload.address is not None:
        vendor.address = payload.address

    db.commit()
    db.refresh(vendor)
    return vendor

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    deleted = VendorRepository.delete(db, vendor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"message": "Vendor deleted successfully"}
