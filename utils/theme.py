
import streamlit as st


PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"

BACKGROUND = "#F8FAFC"
CARD = "#FFFFFF"

TEXT = "#111827"
TEXT_SECONDARY = "#6B7280"

BORDER = "#E5E7EB"


def apply_theme(accent_color=PRIMARY):

    st_css = f"""
    <style>

    .stApp {{
        background-color:{BACKGROUND};
    }}

    section[data-testid="stSidebar"] {{
        background-color:{CARD};
    }}

    h1,h2,h3 {{
        color:{TEXT};
    }}

    .stButton button {{
        background-color:{accent_color};
        color:white;
        border-radius:10px;
        font-weight:600;
    }}

    </style>
    """

    st.markdown(
        st_css,
        unsafe_allow_html=True
    )
