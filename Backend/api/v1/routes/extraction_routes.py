from fastapi import APIRouter, HTTPException, Query
from services.ocr_service import OCRService
from services.llm_extraction_service import LLMExtractionService
from services.validation_service import ValidationService
from services.mapping_service import MappingService
import os

router = APIRouter(tags=["Extraction"])

@router.get("/invoice-data")
def extract_invoice_data(file_path: str = Query(...)):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # 1. OCR
    raw_text = OCRService.extract_text(file_path)

    # 2. LLM structured extraction
    structured = LLMExtractionService.extract_invoice_data(raw_text)

    # 3. Validation & normalization
    validated = ValidationService.validate_invoice(structured)

    # 4. Vendor mapping (returns vendor_id)
    vendor_id = MappingService.map_vendor(validated.get("vendor_name", "Unknown Vendor"))
    validated["vendor_id"] = vendor_id

    return {
        "file_path": file_path,
        "raw_text": raw_text,
        "structured_data": validated
    }
