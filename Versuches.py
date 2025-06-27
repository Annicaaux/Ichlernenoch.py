import streamlit as st

# --- Seiten-Setup ---
st.set_page_config(page_title="Freud ist ein Pups", layout="wide")

# --- Titel der App ---
st.title("Freud ist ein Pups")

# --- Globales CSS Styling ---
st.markdown("""
    <style>
        html, body, [class*="st"] {
            background-color: #f5f5dc;
            font-family: ´Marker Felt´, fantasy;
            color: 	#8b6914;
        }

    </style>
""", unsafe_allow_html=True)
