import streamlit as st
import plotly.express as px
import pandas as pd
from components.header import render_header

from db.connection import get_engine
from queries.demand import (
    rides_by_hour,
    rides_by_day,
    rides_heatmap
)

st.set_page_config(layout="wide")
render_header()
st.title("Demand Analysis")

engine = get_engine()

# ---------- DATA ----------
hour_df = rides_by_hour(engine)
day_df = rides_by_day(engine)
heat_df = rides_heatmap(engine)

# Clean weekday names
day_df["day"] = day_df["day"].str.strip()
heat_df["day"] = heat_df["dow"].map({
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
})

# ---------- PEAK INSIGHTS ----------
peak_hour = hour_df.loc[hour_df["rides"].idxmax()]
peak_day = day_df.loc[day_df["rides"].idxmax()]

# ---------- KPIs ----------
col1, col2 = st.columns(2)
col1.metric("Peak Hour", f"{int(peak_hour['hour'])}:00")
col2.metric("Busiest Day", peak_day["day"])

st.divider()

# ---------- CHARTS ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rides by Hour of Day")
    fig1 = px.bar(
        hour_df,
        x="hour",
        y="rides",
        labels={"hour": "Hour of Day", "rides": "Total Rides"}
    )
    fig1.update_layout(height=350)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Rides by Day of Week")
    fig2 = px.bar(
        day_df,
        x="day",
        y="rides",
        labels={"day": "Day", "rides": "Total Rides"}
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------- HEATMAP ----------
st.subheader("Demand Heatmap (Day × Hour)")

pivot = heat_df.pivot_table(
    index="day",
    columns="hour",
    values="rides",
    fill_value=0
)

fig3 = px.imshow(
    pivot,
    aspect="auto",
    labels=dict(color="Rides")
)

fig3.update_layout(height=420)
st.plotly_chart(fig3, use_container_width=True)

# ---------- INSIGHTS ----------
st.subheader("Key Demand Insights")
st.success(f"Peak demand occurs at **{int(peak_hour['hour'])}:00 hours**")
st.info(f"**{peak_day['day']}** is the busiest day overall")
st.warning("Consider increasing driver supply during peak windows")