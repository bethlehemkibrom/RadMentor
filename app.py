
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color
from utils.components import section_title, info_card


st.set_page_config(
    page_title="RadMentor",
    page_icon="R",
    layout="wide"
)


current_color = get_accent_color()


accent = st.sidebar.color_picker(
    "Accent colour",
    current_color
)


if accent != current_color:
    save_accent_color(accent)
    st.rerun()


apply_theme(accent)


st.markdown(
    f"""
    <div style="
        background:white;
        padding:50px;
        border-radius:24px;
        border:1px solid #E5E7EB;
        border-left:8px solid {accent};
        box-shadow:0 6px 20px rgba(0,0,0,0.06);
        text-align:center;
    ">

    <h1 style="
        color:{accent};
        font-size:42px;
        margin-bottom:10px;
    ">
    RadMentor
    </h1>

    <h3 style="
        color:#111827;
        font-weight:500;
    ">
    Your personal radiology learning workspace
    </h3>

    <p style="
        color:#6B7280;
        font-size:18px;
        margin-top:20px;
    ">
    Capture cases, review findings, track progress,
    and build your personal radiology knowledge library.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


section_title("Start Learning")


col1, col2, col3 = st.columns(3)


with col1:
    info_card(
        "Add Cases",
        "Save important radiology cases, findings, diagnoses, and teaching points."
    )


with col2:
    info_card(
        "Review Library",
        "Revisit previous cases and strengthen your diagnostic reasoning."
    )


with col3:
    info_card(
        "Track Progress",
        "Monitor your learning journey and identify areas for improvement."
    )


section_title("Why RadMentor?")


st.markdown(
    """
    <div style="
        background:white;
        border:1px solid #E5E7EB;
        border-radius:16px;
        padding:24px;
        color:#374151;
        font-size:16px;
    ">

    Radiology expertise develops through exposure,
    reflection, and repetition.

    RadMentor helps transform individual cases into
    a structured learning system that grows with you.

    </div>
    """,
    unsafe_allow_html=True
)
