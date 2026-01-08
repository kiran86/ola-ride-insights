import streamlit as st
import plotly.express as px

from db.connection import get_engine
from queries.ratings import (
    rating_kpis,
    rating_distribution,
    ratings_by_vehicle
)

st.set_page_config(layout="wide")
st.title("Ratings & Experience")

engine = get_engine()

# ---------- DATA ----------
kpi_df = rating_kpis(engine)
dist_df = rating_distribution(engine)
vehicle_df = ratings_by_vehicle(engine)

cust_avg = kpi_df["avg_customer_rating"][0]
driver_avg = kpi_df["avg_driver_rating"][0]
rating_gap = cust_avg - driver_avg

# ---------- KPIs ----------
col1, col2, col3 = st.columns(3)

col1.metric("Avg Customer Rating", cust_avg)
col2.metric("Avg Driver Rating", driver_avg)
col3.metric("Rating Gap", f"{rating_gap:.2f}")

st.divider()

# ---------- DISTRIBUTION ----------
st.subheader("Rating Distribution")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(
        dist_df,
        x="customer_rating",
        nbins=10,
        title="Customer Ratings"
    )
    fig1.update_layout(height=350)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(
        dist_df,
        x="driver_rating",
        nbins=10,
        title="Driver Ratings"
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- VEHICLE COMPARISON ----------
st.subheader("Ratings by Vehicle Type")

fig3 = px.bar(
    vehicle_df,
    x="vehicle_type",
    y=["avg_customer_rating", "avg_driver_rating"],
    barmode="group",
    labels={"value": "Average Rating", "variable": "Rating Type"}
)
fig3.update_layout(height=380)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ---------- CORRELATION ----------
st.subheader("Customer vs Driver Rating Relationship")

fig4 = px.scatter(
    dist_df,
    x="customer_rating",
    y="driver_rating",
    trendline="ols",
    labels={
        "customer_rating": "Customer Rating",
        "driver_rating": "Driver Rating"
    }
)
fig4.update_layout(height=420)
st.plotly_chart(fig4, use_container_width=True)

# ---------- INSIGHTS ----------
worst_vehicle = vehicle_df.sort_values("avg_customer_rating").iloc[0]

st.subheader("Key Experience Insights")
st.success(
    "Overall ratings indicate a generally positive ride experience"
)
st.info(
    f"**{worst_vehicle['vehicle_type']}** has the lowest average customer rating"
)
st.warning(
    "Rating gaps may indicate mismatched service expectations or operational inconsistencies"
)
