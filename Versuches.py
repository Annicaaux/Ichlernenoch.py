import streamlit as st

# --- Seiten-Setup ---
st.set_page_config(page_title="Freud ist ein Pups", layout="wide")

# --- Globales CSS Styling ---
st.markdown("""
    <style>
        html, body, [class*="st"] {
            background-color: #f5f5dc;
            font-family: 'Marker Felt', fantasy;
            color: #8b6914;
        }
        
        /* Spezielle Styling für den Titel */
        .title-custom {
            font-family: 'Marker Felt', 'Bradley Hand', 'Brush Script MT', cursive, fantasy;
            font-size: 3rem;
            font-weight: bold;
            color: #8b6914;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 2rem;
        }
        
        /* Alternative: Streamlit's eingebaute Titel-Klasse überschreiben */
        .stTitle > h1 {
            font-family: 'Marker Felt', 'Bradley Hand', 'Brush Script MT', cursive, fantasy !important;
            font-size: 4rem !important;
            letter-spacing: 1px !important;
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Option 1: Custom HTML Titel ---
st.markdown('<h1 class="title-custom">Freud ist ein Pups</h1>', unsafe_allow_html=True)

# --- Option 2: Normaler Streamlit Titel (wird durch CSS überschrieben) ---
# st.title("Freud ist ein Pups")
