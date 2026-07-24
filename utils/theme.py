
import streamlit as st


def apply_theme(accent_color="#C98295"):

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-color: #FAF8F8;
        }}


        h1, h2, h3 {{
            color: {accent_color} !important;
        }}


        .stButton button {{
            background-color: {accent_color};
            color: white;
            border-radius: 12px;
            border: none;
            padding: 8px 16px;
        }}


        .stMetric {{
            background-color: white;
            border-radius: 15px;
            padding: 15px;
            border-left: 6px solid {accent_color};
        }}


        [data-testid="stSidebar"] {{
            background-color: white;
            border-right: 3px solid {accent_color};
        }}


        </style>
        """,
        unsafe_allow_html=True
    )
