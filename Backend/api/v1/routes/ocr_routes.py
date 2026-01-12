from fastapi import APIRouter, Query, HTTPException
from services.ocr_service import OCRService
import os

router = APIRouter(tags=["OCR"])

@router.get("/text")
def extract_text(file_path: str = Query(..., description="Path of file in storage/uploads")):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    text = OCRService.extract_text(file_path)
    return {
        "file_path": file_path,
        "extracted_text": text
    }
