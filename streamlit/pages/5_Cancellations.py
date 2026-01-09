import streamlit as st
import plotly.express as px
from components.header import render_header
from db.connection import get_engine
from queries.cancellations import (
    cancellation_kpis,
    cancellation_by_type,
    cancellation_reasons,
    vehicle_cancellations
)

st.set_page_config(layout="wide")
render_header()
st.title("Cancellations Analysis")
engine = get_engine()

# ---------- DATA ----------
kpi_df = cancellation_kpis(engine)
type_df = cancellation_by_type(engine)
vehicle_df = vehicle_cancellations(engine)

total_rides = kpi_df["total_rides"][0]
cancelled = kpi_df["cancelled_rides"][0]
cancel_rate = cancelled / total_rides * 100

# ---------- KPIs ----------
col1, col2, col3 = st.columns(3)
col1.metric("Total Rides", int(total_rides))
col2.metric("Cancelled Rides", int(cancelled))
col3.metric("Cancellation Rate", f"{cancel_rate:.2f}%")

st.divider()

# ---------- CUSTOMER vs DRIVER ----------
st.subheader("Who Cancels Rides?")

fig1 = px.pie(
    type_df,
    names="cancelled_by",
    values="rides",
    hole=0.45
)
fig1.update_layout(height=350)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ---------- REASON TOGGLE ----------
cancel_type = st.radio(
    "View cancellation reasons by:",
    ["Customer", "Driver"],
    horizontal=True
)

reason_df = cancellation_reasons(engine, cancel_type)

st.subheader(f"{cancel_type} Cancellation Reasons")

fig2 = px.bar(
    reason_df,
    x="rides",
    y="reason",
    orientation="h"
)
fig2.update_layout(height=420)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- VEHICLE IMPACT ----------
st.subheader("Cancellations by Vehicle Type")

fig3 = px.bar(
    vehicle_df,
    x="vehicle_type",
    y="cancelled_rides",
    text_auto=True
)
fig3.update_layout(height=380)
st.plotly_chart(fig3, use_container_width=True)

# ---------- INSIGHTS ----------
top_customer_reason = cancellation_reasons(engine, "Customer").iloc[0]["reason"]
top_driver_reason = cancellation_reasons(engine, "Driver").iloc[0]["reason"]
top_vehicle = vehicle_df.iloc[0]["vehicle_type"]

st.subheader("Key Cancellation Insights")
st.warning(
    f"Top customer cancellation reason: **{top_customer_reason}**"
)
st.warning(
    f"Top driver cancellation reason: **{top_driver_reason}**"
)
st.info(
    f"**{top_vehicle}** experiences the highest number of cancellations"
)
st.success(
    "Reducing wait time and improving driver availability can significantly lower cancellations"
)
