import streamlit as st
import pandas as pd
from api_client import get_vendors

st.title("🏢 Vendors")

vendors = get_vendors()

if isinstance(vendors, list) and len(vendors) > 0:
    df = pd.DataFrame(vendors)
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No vendors found.")
