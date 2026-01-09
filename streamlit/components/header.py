import streamlit as st

def render_header():
    st.markdown(
        """
        <style>
        .ola-header {
            background-color: var(--background-color);
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border: 1px solid var(--secondary-background-color);
        }
        .ola-title {
            color: var(--text-color);
            margin: 0;
            font-size: 2rem;
            font-weight: 700;
        }
        .ola-subtitle {
            color: var(--text-color);
            opacity: 0.7;
            margin-top: 0.25rem;
            font-size: 0.95rem;
        }
        </style>

        <div class="ola-header">
            <div class="ola-title">Ola Ride Insights</div>
            <div class="ola-subtitle">
                Data-driven insights into demand, revenue, and ride experience
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
