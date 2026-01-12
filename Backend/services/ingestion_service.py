import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "storage/uploads"

class IngestionService:

    @staticmethod
    async def save_file(file: UploadFile) -> str:
        # ensure uploads dir exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # create unique file name
        file_ext = file.filename.split(".")[-1]
        unique_name = f"{uuid.uuid4()}.{file_ext}"

        file_path = os.path.join(UPLOAD_DIR, unique_name)

        # save file
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return file_path
