import streamlit as st

def sidebar_filters():
    st.sidebar.header("Filters")
    return {
        "completed_only": st.sidebar.checkbox("Completed rides only", True)
    }
