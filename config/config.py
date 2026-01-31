import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
HF_TOKEN = st.secrets["HF_TOKEN"]

MODEL_NAME = "groq:qwen/qwen3-32b"
