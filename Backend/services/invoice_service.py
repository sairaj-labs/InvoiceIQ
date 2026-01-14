from repositories.vendor_repository import VendorRepository
from repositories.invoice_repository import InvoiceRepository
from repositories.item_repository import ItemRepository
from models.item import Item

class InvoiceService:

    @staticmethod
    def process_invoice(db, structured_data: dict, file_path: str):
        # 1. Vendor handling
        vendor_name = structured_data.get("vendor_name", "Unknown Vendor")
        vendor = VendorRepository.get_by_name(db, vendor_name)

        if not vendor:
            vendor = VendorRepository.create(db, name=vendor_name)

        # 2. Invoice creation
        invoice_data = {
            "vendor_id": vendor.id,
            "invoice_number": structured_data.get("invoice_number"),
            "invoice_date": structured_data.get("invoice_date"),
            "subtotal": structured_data.get("subtotal"),
            "tax": structured_data.get("tax"),
            "total": structured_data.get("total"),
            "currency": structured_data.get("currency"),
        }

        invoice = InvoiceRepository.create(db, invoice_data)

        # 3. Items creation
        items_data = structured_data.get("items", [])
        item_objects = []

        for item in items_data:
            item_objects.append(Item(
                invoice_id=invoice.id,
                description=item.get("description"),
                quantity=item.get("quantity"),
                rate=item.get("rate"),
                tax_percent=None,   # LLM may not extract this yet
                amount=item.get("amount")
            ))

        if item_objects:
            ItemRepository.bulk_create(db, item_objects)

        return invoice, vendor
