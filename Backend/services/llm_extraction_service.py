import json
import google.generativeai as genai
from core.config import settings

class LLMExtractionService:

    @staticmethod
    def extract_invoice_data(ocr_text: str) -> dict:
        # Configure Gemini with API Key
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # Structured Extraction Prompt
        prompt = f"""
        You are an invoice data extraction engine.
        Extract the following fields from the invoice text and return ONLY valid JSON with double quotes:

        Fields:
        - vendor_name (string)
        - invoice_number (string)
        - invoice_date (string)
        - subtotal (number)
        - tax (number)
        - total (number)
        - currency (string)
        - items: array of objects with fields: description, quantity, rate, amount

        If any field is missing in the text, set it to null or an empty array for items.

        Invoice text:
        {ocr_text}

        Respond with only valid JSON. No markdown, no extra text.
        """

        # Call Gemini
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(prompt)

        # Parse JSON response
        try:
            result = json.loads(response.text)
        except json.JSONDecodeError:
            # fallback: try to extract JSON manually if formatting issues
            json_str = response.text[response.text.find("{"):response.text.rfind("}")+1]
            result = json.loads(json_str)

        return result
