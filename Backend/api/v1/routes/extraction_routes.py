from fastapi import APIRouter, HTTPException, Query
from services.ocr_service import OCRService
from services.llm_extraction_service import LLMExtractionService
import os

router = APIRouter(tags=["Extraction"])

@router.get("/invoice-data")
def extract_invoice_data(file_path: str = Query(...)):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # OCR step
    text = OCRService.extract_text(file_path)

    # LLM extraction step
    structured = LLMExtractionService.extract_invoice_data(text)

    return {
        "file_path": file_path,
        "raw_text": text,
        "structured_data": structured
    }
