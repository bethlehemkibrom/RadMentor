
import streamlit as st


PRIMARY = "#2563EB"
PRIMARY_DARK = "#1E40AF"

BACKGROUND = "#F8FAFC"
CARD = "#FFFFFF"

TEXT = "#0F172A"
TEXT_SECONDARY = "#64748B"

BORDER = "#E2E8F0"



def apply_theme(accent_color=PRIMARY):

    css = f"""

    <style>

    /* Main background */

    .stApp {{
        background:
        linear-gradient(
            180deg,
            #F8FAFC 0%,
            #EFF6FF 100%
        );

        color:{TEXT};
    }}


    /* Remove top padding */

    .block-container {{
        padding-top:2rem;
        padding-bottom:3rem;
        max-width:1200px;
    }}


    /* Sidebar */

    section[data-testid="stSidebar"] {{

        background:
        linear-gradient(
            180deg,
            #FFFFFF,
            #F8FAFC
        );

        border-right:1px solid {BORDER};

    }}


    section[data-testid="stSidebar"] h1 {{

        color:{PRIMARY};

    }}



    /* Headers */

    h1 {{

        font-size:48px !important;
        font-weight:800 !important;
        letter-spacing:-1px;

    }}


    h2 {{

        font-weight:700 !important;

    }}


    h3 {{

        font-weight:700 !important;

    }}



    /* Buttons */

    .stButton button {{

        background:
        linear-gradient(
            135deg,
            {accent_color},
            {PRIMARY_DARK}
        );

        color:white;

        border:none;

        border-radius:14px;

        padding:
        0.6rem 1.5rem;

        font-weight:700;

        transition:.2s;

    }}


    .stButton button:hover {{

        transform:translateY(-2px);

        box-shadow:
        0 8px 20px rgba(37,99,235,.25);

    }}



    /* Inputs */

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div {{

        border-radius:12px;

        border:1px solid {BORDER};

    }}



    /* Cards */

    .card {{

        background:{CARD};

        border-radius:22px;

        border:
        1px solid {BORDER};

        padding:25px;

        box-shadow:
        0 10px 30px
        rgba(15,23,42,.06);

    }}



    /* Metrics */

    div[data-testid="metric-container"] {{

        background:white;

        border-radius:18px;

        padding:20px;

        border:
        1px solid {BORDER};

        box-shadow:
        0 8px 25px
        rgba(15,23,42,.05);

    }}



    /* Hide Streamlit footer */

    footer {{

        visibility:hidden;

    }}



    </style>

    """

    st.markdown(
        css,
        unsafe_allow_html=True
    )
