from fastapi import APIRouter, UploadFile, File, Depends
from services.ingestion_service import IngestionService
from services.ocr_service import OCRService
from services.llm_extraction_service import LLMExtractionService
from services.validation_service import ValidationService
from services.invoice_service import InvoiceService
from db.connection import get_db

router = APIRouter(tags=["Process Invoice"])

@router.post("/invoice")
async def process_invoice(file: UploadFile = File(...), db=Depends(get_db)):
    
    # Step 1: Save file
    saved_path = await IngestionService.save_file(file)

    # Step 2: OCR
    raw_text = OCRService.extract_text(saved_path)

    # Step 3: LLM Structuring
    structured = LLMExtractionService.extract_invoice_data(raw_text)

    # Step 4: Validation
    validated = ValidationService.validate_invoice(structured)

    # Step 5: DB Save
    invoice, vendor = InvoiceService.process_invoice(db, validated, saved_path)

    return {
        "status": "success",
        "invoice_id": invoice.id,
        "vendor_id": vendor.id
    }
