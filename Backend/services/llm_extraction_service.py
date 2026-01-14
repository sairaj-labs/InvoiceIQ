import json
from google.genai import Client
from core.config import settings

class LLMExtractionService:

    @staticmethod
    def extract_invoice_data(ocr_text: str) -> dict:
        client = Client(api_key=settings.GEMINI_API_KEY)

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

        If any field is missing, set it to null or an empty array for items.
        Respond with only valid JSON, no markdown, no explanation.

        Invoice text:
        {ocr_text}
        """

        # Call Gemini
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

        # Extract raw text
        text_output = response.text.strip()

        # Parse JSON
        try:
            return json.loads(text_output)
        except json.JSONDecodeError:
            # fallback to extract just JSON block
            json_str = text_output[text_output.find("{"):text_output.rfind("}")+1]
            return json.loads(json_str)
