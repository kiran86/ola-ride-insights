import streamlit as st
from db.connection import get_engine
from queries.metrics import total_kpis, rides_by_vehicle
from components.kpis import show_kpis
from components.charts import vehicle_revenue_chart
from components.filters import sidebar_filters

st.set_page_config(
    page_title="Ola Ride Insights",
    layout="wide"
)

st.title("Ola Ride Insights Dashboard")

engine = get_engine()
filters = sidebar_filters()

kpi_df = total_kpis(engine)
vehicle_df = rides_by_vehicle(engine)

show_kpis(kpi_df)
st.divider()
vehicle_revenue_chart(vehicle_df)