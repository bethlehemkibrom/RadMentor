
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color


st.set_page_config(
    page_title="RadMentor",
    page_icon="🩻",
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
<style>

@keyframes fadeUp {{
from {{
opacity:0;
transform:translateY(40px);
}}
to {{
opacity:1;
transform:translateY(0);
}}
}}

@keyframes float {{
0% {{transform:translateY(0);}}
50% {{transform:translateY(-15px);}}
100% {{transform:translateY(0);}}
}}

@keyframes moveBackground {{
0% {{background-position:0% 50%;}}
50% {{background-position:100% 50%;}}
100% {{background-position:0% 50%;}}
}}


.hero {{
animation:fadeUp 1.2s ease;

background:linear-gradient(
120deg,
#ffffff,
#eff6ff,
#dbeafe
);

background-size:300% 300%;
animation:moveBackground 8s infinite;

padding:50px 30px;
border-radius:35px;
border-left:10px solid {accent};

box-shadow:
0 20px 50px rgba(0,0,0,0.08);

overflow:hidden;
}}


.icon {{
font-size:70px;
animation:float 3s infinite;
}}


.title {{
font-size:clamp(35px,6vw,60px);
font-weight:900;
color:{accent};
word-wrap:break-word;
}}


.subtitle {{
font-size:clamp(16px,3vw,24px);
color:#475569;
}}


.feature {{
animation:fadeUp 1.5s ease;

background:white;

padding:25px;

border-radius:25px;

min-height:170px;

border:1px solid #e5e7eb;

box-shadow:
0 10px 30px rgba(0,0,0,0.06);

transition:0.3s;

overflow:hidden;
}}


.feature:hover {{
transform:translateY(-10px);
box-shadow:
0 20px 40px rgba(0,0,0,0.12);
}}


.feature h3 {{
color:{accent};
font-size:22px;
}}


</style>
""",
unsafe_allow_html=True
)


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

<p style="font-size:18px;">
Every image is a story. Every case is an opportunity to learn.
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")


c1,c2,c3 = st.columns(3)


for col,title,text in [
    (c1,"Clinical Case Library",
     "Organize imaging cases and build your personal knowledge base."),
    (c2,"Smart Review",
     "Revisit cases and strengthen diagnostic memory."),
    (c3,"Professional Growth",
     "Track your journey toward radiology mastery.")
]:

    with col:
        st.markdown(
        f"""
        <div class="feature">

        <h3>{title}</h3>

        <p>
        {text}
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
Where images become expertise
</h2>

<p class="subtitle">
A modern learning environment designed for future radiologists.
</p>

</div>
""",
unsafe_allow_html=True
)
