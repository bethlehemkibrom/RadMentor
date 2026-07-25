
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color


st.set_page_config(
    page_title="RadMentor",
    page_icon="🩻",
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


# Premium animations + styling

st.markdown(
f"""
<style>

@keyframes fade {{
0% {{
opacity:0;
transform:translateY(25px);
}}

100% {{
opacity:1;
transform:translateY(0);
}}
}}

@keyframes float {{
0% {{transform:translateY(0px);}}
50% {{transform:translateY(-12px);}}
100% {{transform:translateY(0px);}}
}}

.hero {{
animation:fade 1.2s ease;
background:linear-gradient(135deg,#ffffff,#eff6ff);
padding:70px 40px;
border-radius:35px;
text-align:center;
border-left:10px solid {accent};
box-shadow:0 20px 50px rgba(0,0,0,0.08);
}}

.icon {{
font-size:90px;
animation:float 3s infinite;
}}

.title {{
font-size:60px;
font-weight:900;
color:{accent};
}}

.subtitle {{
font-size:24px;
color:#475569;
}}

.feature {{
background:white;
padding:30px;
border-radius:25px;
height:190px;
border:1px solid #e5e7eb;
box-shadow:0 10px 30px rgba(0,0,0,0.06);
animation:fade 1.5s ease;
}}

.feature h3 {{
color:{accent};
}}

</style>
""",
unsafe_allow_html=True
)


# Hero

st.markdown(
f"""
<div class="hero">

<div class="icon">
🩻
</div>

<div class="title">
RadMentor
</div>

<div class="subtitle">
Master radiology through cases, reflection, and intelligent learning
</div>

<br>

<p style="font-size:19px;">
Your personal radiology knowledge companion.
Capture cases. Review findings. Grow confidence.
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")


# Feature cards

c1,c2,c3 = st.columns(3)


with c1:
    st.markdown(
    f"""
    <div class="feature">
    <h3>Clinical Case Library</h3>
    <p>
    Build your own collection of imaging cases
    and teaching points.
    </p>
    </div>
    """,
    unsafe_allow_html=True
    )


with c2:
    st.markdown(
    f"""
    <div class="feature">
    <h3>Smart Review</h3>
    <p>
    Strengthen memory through structured
    case repetition.
    </p>
    </div>
    """,
    unsafe_allow_html=True
    )


with c3:
    st.markdown(
    f"""
    <div class="feature">
    <h3>Professional Growth</h3>
    <p>
    Track your journey toward diagnostic confidence.
    </p>
    </div>
    """,
    unsafe_allow_html=True
    )


st.write("")


st.markdown(
f"""
<div class="hero">

<h2 style="color:{accent};">
Built for the next generation of radiologists
</h2>

<p class="subtitle">
A place where every image becomes a learning opportunity.
</p>

</div>
""",
unsafe_allow_html=True
)
