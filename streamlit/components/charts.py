import streamlit as st

def vehicle_revenue_chart(df):
    st.subheader("Revenue by Vehicle Type")
    st.bar_chart(
        df.set_index("vehicle_type")[["revenue"]],
        use_container_width=True
    )
