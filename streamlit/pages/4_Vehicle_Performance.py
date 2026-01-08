import streamlit as st
import plotly.express as px

from db.connection import get_engine
from queries.vehicle import vehicle_kpis

st.set_page_config(layout="wide")
st.title("Vehicle Performance")

engine = get_engine()
df = vehicle_kpis(engine)

# ---------- VEHICLE SELECT ----------
vehicle_list = ["All"] + sorted(df["vehicle_type"].unique().tolist())
selected_vehicle = st.selectbox("Select Vehicle Type", vehicle_list)

if selected_vehicle != "All":
    df_filtered = df[df["vehicle_type"] == selected_vehicle]
else:
    df_filtered = df

# ---------- KPIs ----------
total_rides = int(df_filtered["total_rides"].sum())
total_revenue = df_filtered["revenue"].sum()
avg_distance = df_filtered["avg_distance"].mean()
avg_rating = df_filtered["avg_rating"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", total_rides)
col2.metric("Revenue", f"₹ {total_revenue:,.0f}")
col3.metric("Avg Distance (km)", f"{avg_distance:.1f}")
col4.metric("Avg Rating", f"{avg_rating:.2f}")

st.divider()

# ---------- REVENUE BY VEHICLE ----------
st.subheader("Revenue by Vehicle Type")

fig1 = px.bar(
    df,
    x="vehicle_type",
    y="revenue",
    text_auto=".2s",
    color="vehicle_type"
)
fig1.update_layout(height=380)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ---------- RIDES VS DISTANCE ----------
st.subheader("Ride Volume vs Average Distance")

fig2 = px.scatter(
    df,
    x="avg_distance",
    y="total_rides",
    size="revenue",
    color="vehicle_type",
    labels={
        "avg_distance": "Average Ride Distance (km)",
        "total_rides": "Total Rides"
    }
)
fig2.update_layout(height=420)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- VEHICLE TABLE ----------
st.subheader("Vehicle Performance Summary")

st.dataframe(
    df.sort_values("revenue", ascending=False),
    use_container_width=True
)

# ---------- INSIGHTS ----------
top_vehicle = df.iloc[0]
low_util_vehicle = df.sort_values("total_rides").iloc[0]

st.subheader("Key Vehicle Insights")
st.success(
    f"**{top_vehicle['vehicle_type']}** generates the highest revenue "
    f"(₹ {top_vehicle['revenue']:,.0f})"
)
st.info(
    f"**{low_util_vehicle['vehicle_type']}** has the lowest ride utilization"
)
st.warning(
    "High-distance vehicles with lower ride counts may need pricing or demand optimization"
)
