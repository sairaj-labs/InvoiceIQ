import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import platform

class OCRService:

    @staticmethod
    def extract_text_from_image(image_path: str) -> str:
        if platform.system() == "Windows":
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        poppler_path = r"C:\Users\Sairaj\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"

        pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

        extracted_text = ""
        for page in pages:
            text = pytesseract.image_to_string(page)
            extracted_text += text + "\n"

        return extracted_text

    @staticmethod
    def extract_text(file_path: str) -> str:
        ext = file_path.split(".")[-1].lower()

        if ext in ["jpg", "jpeg", "png"]:
            return OCRService.extract_text_from_image(file_path)
        elif ext == "pdf":
            return OCRService.extract_text_from_pdf(file_path)
        else:
            raise ValueError("Unsupported file type for OCR")
