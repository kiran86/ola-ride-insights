import streamlit as st
import plotly.express as px
from components.header import render_header

from db.connection import get_engine
from queries.revenue import (
    revenue_kpis,
    revenue_by_payment,
    booking_value_distribution
)

st.set_page_config(layout="wide")
render_header()
st.title("Revenue & Payments")

engine = get_engine()

# ---------- DATA ----------
kpi_df = revenue_kpis(engine)
payment_df = revenue_by_payment(engine)
dist_df = booking_value_distribution(engine)

total_revenue = kpi_df["total_revenue"][0]
avg_booking = kpi_df["avg_booking_value"][0]

# ---------- KPIs ----------
col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"₹ {total_revenue:,.0f}")
col2.metric("Avg Booking Value", f"₹ {avg_booking:,.0f}")

st.divider()

# ---------- CHARTS ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Payment Method Share")
    fig1 = px.pie(
        payment_df,
        names="payment_method",
        values="revenue",
        hole=0.45
    )
    fig1.update_layout(height=350)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Revenue by Payment Method")
    fig2 = px.bar(
        payment_df,
        x="payment_method",
        y="revenue",
        text_auto=".2s"
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- DISTRIBUTION ----------
st.subheader("Booking Value Distribution by Payment Method")

fig3 = px.box(
    dist_df,
    x="payment_method",
    y="booking_value",
    points="outliers"
)
fig3.update_layout(height=420)
st.plotly_chart(fig3, use_container_width=True)

# ---------- INSIGHTS ----------
top_payment = payment_df.iloc[0]

st.subheader("Key Revenue Insights")
st.success(
    f"**{top_payment['payment_method']}** generates the highest revenue "
    f"(₹ {top_payment['revenue']:,.0f})"
)
st.info("Digital payments dominate overall revenue contribution")
st.warning("High-value bookings show significant variance across payment types")
