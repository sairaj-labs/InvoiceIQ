from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ingestion_service import IngestionService

router = APIRouter(tags=["Upload"])

@router.post("/invoice-file")
async def upload_invoice_file(file: UploadFile = File(...)):
    allowed_ext = ["pdf", "png", "jpg", "jpeg"]

    ext = file.filename.split(".")[-1].lower()
    if ext not in allowed_ext:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    saved_path = await IngestionService.save_file(file)

    return {
        "status": "success",
        "file_path": saved_path
    }
