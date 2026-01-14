from datetime import datetime

class ValidationService:

    @staticmethod
    def normalize_date(date_str):
        if not date_str:
            return None

        # try multiple formats
        formats = ["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).date()
            except:
                pass
        return None

    @staticmethod
    def validate_totals(data: dict) -> bool:
        subtotal = data.get("subtotal")
        tax = data.get("tax")
        total = data.get("total")

        if subtotal is None or tax is None or total is None:
            return False

        # allow small rounding tolerance
        return abs((subtotal + tax) - total) < 0.01

    @staticmethod
    def validate_items(data: dict) -> bool:
        items = data.get("items", [])
        for item in items:
            qty = item.get("quantity", 0)
            rate = item.get("rate", 0)
            amount = item.get("amount", 0)
            if abs((qty * rate) - amount) > 0.01:
                return False
        return True

    @staticmethod
    def validate_invoice(data: dict) -> dict:
        # normalize date
        data["invoice_date"] = ValidationService.normalize_date(data.get("invoice_date"))

        # currency fallback
        if not data.get("currency"):
            data["currency"] = "INR"  # default for India

        # calculate flags
        data["validation"] = {
            "totals_valid": ValidationService.validate_totals(data),
            "items_valid": ValidationService.validate_items(data)
        }

        return data
