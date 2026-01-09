import streamlit as st
import plotly.express as px
from components.header import render_header

from db.connection import get_engine
from queries.overview import (
    fetch_overview_kpis,
    fetch_rides_over_time,
    fetch_booking_status
)
from components.kpis import show_overview_kpis

st.set_page_config(layout="wide")
render_header()
st.title("Overview")

engine = get_engine()

# ---------- DATA ----------
kpi_df = fetch_overview_kpis(engine)
rides_time_df = fetch_rides_over_time(engine)
status_df = fetch_booking_status(engine)

# ---------- KPIs ----------
show_overview_kpis(kpi_df)

st.divider()

# ---------- CHARTS ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Ride Volume Over Time")
    fig = px.line(
        rides_time_df,
        x="ride_date",
        y="rides",
        markers=True
    )
    fig.update_layout(height=350, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Booking Status Breakdown")
    fig2 = px.pie(
        status_df,
        names="booking_status",
        values="rides",
        hole=0.4
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- INSIGHTS ----------
peak_day = rides_time_df.loc[rides_time_df["rides"].idxmax()]

st.subheader("Key Insights")
st.success(f"Highest ride volume observed on **{peak_day['ride_date']}**")
st.info("Completed rides contribute the majority of revenue")
st.warning("Cancellations present opportunities for operational improvement")
