from sqlalchemy.orm import Session
from models.vendor import Vendor

class VendorRepository:

    @staticmethod
    def create(db: Session, name: str, gstin: str = None, address: str = None):
        vendor = Vendor(name=name, gstin=gstin, address=address)
        db.add(vendor)
        db.commit()
        db.refresh(vendor)
        return vendor

    @staticmethod
    def get_by_id(db: Session, vendor_id: int):
        return db.query(Vendor).filter(Vendor.id == vendor_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Vendor).all()

    @staticmethod
    def get_by_name(db: Session, name: str):
        return db.query(Vendor).filter(Vendor.name == name).first()
    
    @staticmethod
    def delete(db: Session, vendor_id: int):
        vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
        if vendor:
            db.delete(vendor)
            db.commit()
            return True
        return False
