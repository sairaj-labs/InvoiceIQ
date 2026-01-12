from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings



# Create SQLAlchemy engine for Supabase Postgres
engine = create_engine(settings.DATABASE_URL)

# SessionLocal will be used in routes/services
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
