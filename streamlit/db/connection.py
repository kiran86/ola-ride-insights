import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Create database engine (cached)
@st.cache_resource
def get_engine():

    # Read env variables
    DB_USER = os.getenv("user")
    DB_PASSWORD = quote_plus(os.getenv("password"))
    DB_HOST = os.getenv("host")
    DB_PORT = os.getenv("port")
    DB_NAME = os.getenv("dbname")

    # Build connection URL
    DATABASE_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(DATABASE_URL)