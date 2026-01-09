import streamlit as st

def render_header():
    st.markdown(
        """
        <div style="
            background-color:#F5F7FA;
            padding:15px 20px;
            border-radius:10px;
            margin-bottom:20px;
        ">
            <h1 style="color:#111827; margin:0;">
                Ola Ride Insights
            </h1>
            <p style="color:#6B7280; margin:5px 0 0;">
                Data-driven insights into ride demand, revenue, and experience
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
