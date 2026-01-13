from pydantic_settings import BaseSettings
from pathlib import Path

# Calculate absolute backend directory
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME: str = "InvoiceIQ"
    APP_VERSION: str = "0.1.0"
    DATABASE_URL: str
    GEMINI_API_KEY: str  

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
