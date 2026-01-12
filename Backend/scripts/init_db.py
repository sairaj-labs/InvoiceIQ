import sys
from pathlib import Path

# Add project root to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from db.connection import engine
from models.base import Base

# IMPORTANT: import all models so SQLAlchemy registers them
from models.vendor import Vendor
from models.invoice import Invoice
from models.item import Item

from core.config import settings

def init():
    print("Creating tables in Postgres (Railway)...")
    print("DB URL =", settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Done!")

if __name__ == "__main__":
    init()
