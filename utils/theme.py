
import streamlit as st


"""
RadMentor Design System v1.0
Premium clinical interface styling
"""


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
        background-color: {BACKGROUND};
        color: {TEXT};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {CARD};
        border-right: 1px solid {BORDER};
    }}

    h1, h2, h3 {{
        color: {TEXT};
    }}

    .stButton button {{
        background-color: {accent_color};
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
