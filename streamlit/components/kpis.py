import streamlit as st

def show_kpis(df):
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rides", int(df["total_rides"][0]))
    col2.metric("Successful Rides", int(df["successful_rides"][0]))
    # Format revenue in Indian Rupees format
    col3.metric("Revenue", f"₹ {df['revenue'][0]:,.0f}")
