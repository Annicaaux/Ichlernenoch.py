import streamlit as st
from datetime import datetime
import random

# --- Seiten-Setup ---
st.set_page_config(page_title="Guck mal Mommy", layout="narrow")

# --- Titel der App ---
st.title("Guck mal Mommy")

# --- Globales CSS Styling ---
st.markdown("""
    <style>
        html, body, [class*="st"] {
            background-color: #fdf6ee;
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            color: #2f2f2f;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            color: #3b3b3b;
        }

        .postit {
            font-family: 'Patrick Hand', 'Comic Sans MS', cursive;
        }
    </style>
""", unsafe_allow_html=True)
