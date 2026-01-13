from pdf2image import convert_from_path

pdf_path = r"C:\Users\Sairaj\Desktop\InvoiceIQ\InvoiceIQ_main\Backend\storage\uploads\d78e6571-6968-470b-b8d8-96a08195ee6f.pdf"  # change to your PDF filename
poppler_path = r"C:\Users\Sairaj\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"

try:
    pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"SUCCESS: Converted {len(pages)} page(s)")
    pages[0].save("page.png", "PNG")
    print("Saved first page as page.png")
except Exception as e:
    print("ERROR:", e)
