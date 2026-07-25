
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

SUCCESS = "#10B981"
WARNING = "#F59E0B"
ERROR = "#EF4444"

BORDER = "#E5E7EB"


def apply_theme(accent_color=PRIMARY):

    st_css = f"""
    <style>

    .stApp {{
        background-color: {BACKGROUND};
        color: {TEXT};
        font-family: Inter, sans-serif;
    }}

    h1 {{
        color: {TEXT};
        font-size: 34px;
        font-weight: 700;
    }}

    h2 {{
        color: {TEXT};
        font-size: 24px;
        font-weight: 600;
    }}

    h3 {{
        color: {TEXT};
        font-size: 18px;
        font-weight: 600;
    }}

    p {{
        color: {TEXT_SECONDARY};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {CARD};
        border-right: 1px solid {BORDER};
    }}

    div[data-testid="stMetric"] {{
        background-color: {CARD};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 16px;
    }}

    .stButton button {{
        border-radius: 10px;
        border: none;
        background-color: {accent_color};
        color: white;
        font-weight: 600;
        padding: 8px 18px;
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    </style>
    """

    st.markdown(st_css, unsafe_allow_html=True)
