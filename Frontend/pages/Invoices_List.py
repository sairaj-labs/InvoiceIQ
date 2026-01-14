import streamlit as st
import pandas as pd
from api_client import get_invoices, get_invoice

st.title("📄 Invoices List")

invoices = get_invoices()

if isinstance(invoices, list) and len(invoices) > 0:
    df = pd.DataFrame(invoices)
    st.dataframe(df, use_container_width=True)

    selected_id = st.selectbox("Select Invoice ID", df["id"])

    if selected_id:
        details = get_invoice(selected_id)
        st.subheader("Invoice Details")
        st.json(details)
else:
    st.warning("No invoices available.")
