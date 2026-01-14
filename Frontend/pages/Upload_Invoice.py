import streamlit as st
from api_client import process_invoice

st.title("📤 Upload Invoice")

uploaded_file = st.file_uploader("Choose an invoice file", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("Processing invoice..."):
        result = process_invoice(uploaded_file)

    st.success("Invoice processed successfully!")
    st.json(result)
