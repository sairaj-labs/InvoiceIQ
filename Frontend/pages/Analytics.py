import streamlit as st
import pandas as pd
import plotly.express as px
from api_client import get_invoices

st.title("📊 Analytics Dashboard")

invoices = get_invoices()

if isinstance(invoices, list) and len(invoices) > 0:
    df = pd.DataFrame(invoices)

    df["invoice_date"] = pd.to_datetime(df["invoice_date"])

    st.subheader("📅 Monthly Spend")
    monthly = df.groupby(df["invoice_date"].dt.to_period("M")).total.sum()
    st.line_chart(monthly)

    st.subheader("🏢 Spend by Vendor")
    vendor_spend = df.groupby("vendor_id").total.sum()
    st.bar_chart(vendor_spend)
else:
    st.warning("No invoices to analyze.")
