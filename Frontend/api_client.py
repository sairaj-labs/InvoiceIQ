import requests

API_BASE = "http://localhost:8000/api/v1"

def process_invoice(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    r = requests.post(f"{API_BASE}/process/invoice", files=files)
    return r.json()

def safe_json(r):
    try:
        return r.json()
    except Exception:
        print("Non-JSON response:", r.text)
        return None
    
def get_invoices():
    r = requests.get(f"{API_BASE}/invoices")
    print("STATUS:", r.status_code)
    print("RAW RESPONSE:", r.text)  # debug
    try:
        return r.json()
    except:
        return None


def get_invoice(invoice_id: int):
    r = requests.get(f"{API_BASE}/invoices/{invoice_id}")
    return r.json()

def get_vendors():
    r = requests.get(f"{API_BASE}/vendors")
    return r.json()
