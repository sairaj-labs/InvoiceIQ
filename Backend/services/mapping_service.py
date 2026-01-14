from rapidfuzz import fuzz
from repositories.vendor_repository import VendorRepository

class MappingService:
    # temporary in-memory store
    vendor_db = {}   # { normalized_name: vendor_id }
    next_id = 1

    @staticmethod
    def normalize_name(name: str) -> str:
        return name.lower().strip()

    @staticmethod
    def map_vendor(vendor_name: str) -> int:
        normalized = MappingService.normalize_name(vendor_name)

        # If vendor exists return ID
        if normalized in MappingService.vendor_db:
            return MappingService.vendor_db[normalized]

        # Else insert new vendor
        vendor_id = MappingService.next_id
        MappingService.vendor_db[normalized] = vendor_id
        MappingService.next_id += 1
        return vendor_id
