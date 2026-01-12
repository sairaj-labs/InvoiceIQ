import pytesseract
from PIL import Image
import subprocess
import platform

class OCRService:

    @staticmethod
    def extract_text(image_path: str) -> str:
        # For Windows systems we may need to specify tesseract path
        if platform.system() == "Windows":
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # Open image file for OCR
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
