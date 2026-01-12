from sqlalchemy import Column, Integer, String
from .base import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gstin = Column(String, nullable=True)
    address = Column(String, nullable=True)
