import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="10.0.0.2",
    database="ola",
    user="root",
    password="m@$t3rm!Nd"
)

st.title("Ola Ride Insights")

query = """
SELECT vehicle_type,
       COUNT(*) AS rides,
       SUM(booking_value)::money AS revenue
FROM rides
WHERE is_incomplete_ride=TRUE
GROUP BY vehicle_type
ORDER BY revenue DESC
"""
df = pd.read_sql(query, conn)

st.dataframe(df)
st.bar_chart(df.set_index("vehicle_type")["revenue"])

st.subheader("Power BI Dashboard")
st.components.v1.iframe(
    "POWER_BI_EMBED_URL",
    height=600
)
