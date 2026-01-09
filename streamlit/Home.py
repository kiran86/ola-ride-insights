import streamlit as st
from components.header import render_header

st.set_page_config(
    layout="wide"
)
render_header()
st.markdown(
    """
    Welcome to the **Ola Ride Insights** analytics dashboard.
    
    Use the navigation on the left to explore demand patterns, vehicle performance,
    revenue trends, cancellations, and service quality.
    """
)

st.info("<= Select a page from the sidebar to begin")