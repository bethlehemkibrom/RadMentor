
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color


st.set_page_config(
    page_title="RadMentor",
    page_icon="🩻"
)


current_color = get_accent_color()


accent = st.sidebar.color_picker(
    "🎨 Choose accent color",
    current_color
)


if accent != current_color:

    save_accent_color(accent)
    st.rerun()


apply_theme(accent)



st.markdown(
    f"""
    <div style="
        text-align:center;
        padding:50px;
        background:white;
        border-radius:24px;
        border-left:8px solid {accent};
        box-shadow:0 6px 20px rgba(0,0,0,0.08);
    ">

    <div style="font-size:60px;">
    🩻
    </div>

    <h1 style="color:{accent};">
    Welcome to RadMentor
    </h1>

    <h3>
    Your personal workspace to learn, reflect, and grow in radiology
    </h3>

    <p style="font-size:18px;">
    Capture cases, review findings,
    and build your radiology knowledge —
    one case at a time.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)



st.divider()


st.subheader(
    "🚀 Start Your Learning Journey"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        "➕ Add Cases\n\n"
        "Save important radiology cases and teaching points."
    )


with col2:

    st.success(
        "📚 Review Cases\n\n"
        "Return to cases and strengthen your memory."
    )


with col3:

    st.warning(
        "📊 Track Progress\n\n"
        "Understand your learning growth."
    )



st.divider()


st.subheader(
    "🧠 Why RadMentor?"
)


st.write(
    """
    Radiology is learned through exposure,
    reflection, and repetition.

    RadMentor helps you organize cases,
    reflect on findings, and create your own
    personal radiology knowledge library.
    """
)
