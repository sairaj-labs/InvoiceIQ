from fastapi import FastAPI
from api.v1.routes.health_routes import router as health_router
from api.v1.routes.vendor_routes import router as vendor_router
from api.v1.routes.invoice_routes import router as invoice_router
from api.v1.routes.upload_routes import router as upload_router
from api.v1.routes.ocr_routes import router as ocr_router
from api.v1.routes.extraction_routes import router as extraction_router
from api.v1.routes.process_routes import router as process_router



import os
print("cwd:", os.getcwd())
print("env_file exists:", os.path.exists(".env"))

app = FastAPI(
    title="InvoiceIQ Backend",
    version="0.1.0"
)

# Register routes
app.include_router(health_router, prefix="/api/v1/health")
app.include_router(vendor_router, prefix="/api/v1/vendors")
app.include_router(invoice_router, prefix="/api/v1/invoices")
app.include_router(upload_router, prefix="/api/v1/upload")
app.include_router(ocr_router, prefix="/api/v1/ocr")
app.include_router(extraction_router, prefix="/api/v1/extract")
app.include_router(process_router, prefix="/api/v1/process")


@app.get("/")
def root():
    return {"message": "InvoiceIQ Backend Running 🚀"}
