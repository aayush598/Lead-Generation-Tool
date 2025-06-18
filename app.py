import streamlit as st
from search import perform_search
from extractor import extract_leads
from export import export_leads
from history import save_to_history, load_history

st.set_page_config(page_title="Lead Generation Tool", layout="wide")
st.title("🔍 Smart Lead Generation Platform")

query = st.text_input("Enter your search query:")
location = st.text_input("Location (optional):")
keywords = st.text_input("Include keywords (comma-separated):")
exclude = st.text_input("Exclude keywords (comma-separated):")
num_results = st.slider("Number of search results", 10, 100, 20)

if st.button("Generate Leads"):
    with st.spinner("Searching and extracting leads..."):
        search_results = perform_search(query, location, keywords, exclude, num_results)
        leads = extract_leads(search_results)
        save_to_history(leads)
    st.success(f"Found {len(leads)} leads.")
    st.dataframe(leads)
    export_leads(leads)

st.markdown("---")
st.header("📅 Lead History")
history = load_history()
if history:
    st.dataframe(history)
else:
    st.write("No leads generated yet.")