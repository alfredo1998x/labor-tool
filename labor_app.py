import streamlit as st

st.set_page_config("Labor Cost Tool", layout="centered")

st.title("🧑‍💼 Labor Cost Calculator")

# Input fields
role = st.text_input("Job Role", placeholder="e.g. Housekeeper")
hours = st.number_input("Hours Worked", min_value=0.0, format="%.2f")
rate = st.number_input("Hourly Rate ($)", min_value=0.0, format="%.2f")

# Calculate cost
if hours and rate:
    total = hours * rate
    st.success(f"Total Labor Cost: **${total:,.2f}**")
