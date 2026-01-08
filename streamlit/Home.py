import streamlit as st

st.set_page_config(
    page_title="Ola Ride Insights",
    layout="wide"
)

st.title("🚖 Ola Ride Insights")
st.markdown(
    """
    Welcome to the **Ola Ride Insights** analytics dashboard.
    
    Use the navigation on the left to explore demand patterns, vehicle performance,
    revenue trends, cancellations, and service quality.
    """
)

st.info("<= Select a page from the sidebar to begin")