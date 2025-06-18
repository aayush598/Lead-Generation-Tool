import streamlit as st
import pandas as pd
import os
from datetime import datetime

def export_leads(leads):
    if leads:
        df = pd.DataFrame(leads)
        filename = f"data/exports/leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df.to_csv(filename, index=False)
        st.download_button("📄 Download CSV", data=df.to_csv(index=False), file_name="leads.csv", mime="text/csv")

