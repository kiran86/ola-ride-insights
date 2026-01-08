import streamlit as st

def show_overview_kpis(df):
    total = int(df["total_rides"][0])
    completed = int(df["completed_rides"][0])
    cancelled = int(df["cancelled_rides"][0])
    revenue = df["revenue"][0]
    rating = df["avg_customer_rating"][0]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Rides", total)
    col2.metric("Completed %", f"{completed / total * 100:.1f}%")
    col3.metric("Cancellation %", f"{cancelled / total * 100:.1f}%")
    col4.metric("Revenue", f"₹ {revenue:,.0f}")
    col5.metric("Avg Rating", rating)
