from sqlalchemy.orm import Session
from models.invoice import Invoice

class InvoiceRepository:

    @staticmethod
    def create(db: Session, data: dict):
        invoice = Invoice(**data)
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def get_by_id(db: Session, invoice_id: int):
        return db.query(Invoice).filter(Invoice.id == invoice_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Invoice).all()

    @staticmethod
    def delete(db: Session, invoice_id: int):
        invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
        if invoice:
            db.delete(invoice)
            db.commit()
            return True
        return False
