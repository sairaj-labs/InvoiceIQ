from sqlalchemy.orm import Session
from models.item import Item

class ItemRepository:

    @staticmethod
    def create(db: Session, data: dict):
        item = Item(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def get_by_invoice(db: Session, invoice_id: int):
        return db.query(Item).filter(Item.invoice_id == invoice_id).all()

    @staticmethod
    def delete_by_invoice(db: Session, invoice_id: int):
        db.query(Item).filter(Item.invoice_id == invoice_id).delete()
        db.commit()
