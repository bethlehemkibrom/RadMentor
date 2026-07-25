
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


# Premium design

st.markdown(
f"""
<style>

@keyframes appear {{
from {{
opacity:0;
transform:translateY(30px);
}}
to {{
opacity:1;
transform:translateY(0);
}}
}}

@keyframes float {{
0%,100% {{
transform:translateY(0);
}}
50% {{
transform:translateY(-12px);
}}
}}

.hero {{
animation:appear 1.2s ease;

background:
linear-gradient(
135deg,
#ffffff,
#f8fafc
);

padding:70px 50px;
border-radius:32px;

border:1px solid #e2e8f0;

box-shadow:
0 20px 50px rgba(15,23,42,0.08);

text-align:center;
}}


.medical-icon {{
font-size:80px;
animation:float 3s infinite;
}}


.hero-title {{
font-size:clamp(40px,6vw,70px);
font-weight:800;
color:{accent};
letter-spacing:-2px;
}}


.hero-text {{
font-size:22px;
color:#475569;
max-width:800px;
margin:auto;
}}


.card {{
background:white;

border-radius:24px;

padding:32px;

border:1px solid #e2e8f0;

box-shadow:
0 10px 30px rgba(15,23,42,0.06);

height:210px;

transition:0.3s;

animation:appear 1.5s ease;
}}


.card:hover {{
transform:translateY(-8px);
box-shadow:
0 20px 45px rgba(15,23,42,0.12);
}}


.card h3 {{
color:{accent};
}}


.number {{
font-size:42px;
font-weight:800;
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

<div class="medical-icon">
🩻
</div>


<div class="hero-title">
RadMentor
</div>


<div class="hero-text">
A personal radiology knowledge system built around
cases, reflection, and lifelong learning.
</div>


<br>

<p>
Capture cases.
Reflect on findings.
Build diagnostic confidence.
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")


# Three pillars

st.markdown(
"## The RadMentor Learning Model"
)


c1,c2,c3 = st.columns(3)


sections = [
(
"01",
"Capture",
"Save meaningful imaging cases, diagnoses, and teaching points."
),
(
"02",
"Reflect",
"Document your reasoning and transform experience into knowledge."
),
(
"03",
"Master",
"Develop stronger diagnostic confidence through structured review."
)
]


for col,(num,title,text) in zip(
    [c1,c2,c3],
    sections
):

    with col:

        st.markdown(
        f"""
        <div class="card">

        <div class="number">
        {num}
        </div>

        <h3>
        {title}
        </h3>

        <p>
        {text}
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


st.write("")


# Features

st.markdown(
"## Designed for Modern Radiology Education"
)


c1,c2,c3 = st.columns(3)


features=[
(
"🩻 Clinical Case Library",
"Build your personal archive of imaging knowledge."
),
(
"📚 Smart Review",
"Strengthen memory through repeated exposure."
),
(
"📊 Learning Insights",
"Understand your growth over time."
)
]


for col,(title,text) in zip(
    [c1,c2,c3],
    features
):

    with col:

        st.markdown(
        f"""
        <div class="card">

        <h3>
        {title}
        </h3>

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
Built for the next generation of radiologists
</h2>

<p class="hero-text">
Where every image becomes a learning opportunity.
</p>

</div>
""",
unsafe_allow_html=True
)
