import streamlit as st

# --- Seiten-Setup ---
st.set_page_config(page_title="Guck mal Mommy", layout="wide")

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

    </style>
""", unsafe_allow_html=True)
