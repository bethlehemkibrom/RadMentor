
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color
from utils.components import section_title, info_card, stat_card


st.set_page_config(
    page_title="RadMentor Dashboard",
    page_icon="R",
    layout="wide"
)


# Theme

current_color = get_accent_color()

accent = st.sidebar.color_picker(
    "Accent colour",
    current_color
)

if accent != current_color:
    save_accent_color(accent)
    st.rerun()

apply_theme(accent)


# Sidebar

st.sidebar.markdown(
    """
    ## RadMentor

    Radiology learning workspace
    """
)


# Hero

st.markdown(
    f"""
    <div style="
        background:white;
        border-radius:24px;
        padding:40px;
        border-left:8px solid {accent};
        border:1px solid #E5E7EB;
    ">

    <h1 style="
        color:{accent};
        font-size:40px;
    ">
    Your Radiology Learning Dashboard
    </h1>

    <p style="
        color:#6B7280;
        font-size:18px;
    ">
    Build knowledge through cases, reflection,
    and structured review.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


# Statistics

section_title("Learning Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    stat_card(
        "Saved Cases",
        "0",
        "Your radiology library"
    )

with col2:
    stat_card(
        "Reviewed",
        "0",
        "Cases completed"
    )

with col3:
    stat_card(
        "Learning Streak",
        "0",
        "Days active"
    )

with col4:
    stat_card(
        "Confidence",
        "New",
        "Diagnostic growth"
    )


# Quick actions

section_title("Quick Actions")


c1, c2, c3 = st.columns(3)


with c1:
    info_card(
        "Add Case",
        "Capture a new radiology case with diagnosis, findings, and learning points."
    )


with c2:
    info_card(
        "Review Library",
        "Return to previous cases and strengthen memory through repetition."
    )


with c3:
    info_card(
        "Learning Dashboard",
        "Understand your progress and identify areas for improvement."
    )


# Recent learning

section_title("Recent Learning")


st.markdown(
    """
    <div style="
        background:white;
        border:1px solid #E5E7EB;
        border-radius:16px;
        padding:25px;
        color:#6B7280;
    ">

    No recent cases yet.

    Start building your personal radiology knowledge library.

    </div>
    """,
    unsafe_allow_html=True
)
