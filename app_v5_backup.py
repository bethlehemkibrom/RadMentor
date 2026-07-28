
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color


st.set_page_config(
    page_title="RadMentor",
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



# Premium CSS

st.markdown(
f"""
<style>

.hero {{

background:
linear-gradient(135deg,#ffffff,#eff6ff);

padding:55px;

border-radius:35px;

border:1px solid #dbeafe;

box-shadow:
0 20px 45px rgba(15,23,42,.08);

}}


.hero h1 {{

font-size:55px;

font-weight:800;

color:#0f172a;

}}


.hero span {{

color:{accent};

}}


.hero p {{

font-size:21px;

color:#475569;

line-height:1.6;

}}



.card {{

background:white;

padding:30px;

border-radius:24px;

border:1px solid #e2e8f0;

box-shadow:
0 8px 25px rgba(0,0,0,.05);

height:200px;

transition:.3s;

}}


.card:hover {{

transform:translateY(-5px);

}}



.card h3 {{

color:{accent};

}}



.progress-card {{

background:
linear-gradient(135deg,{accent},#1e3a8a);

color:white;

padding:35px;

border-radius:28px;

}}



.pearl {{

background:#f8fafc;

padding:35px;

border-radius:25px;

border-left:6px solid {accent};

}}



.activity {{

background:white;

padding:35px;

border-radius:25px;

border:1px dashed #cbd5e1;

text-align:center;

}}



.footer {{

text-align:center;

padding:50px;

color:#64748b;

}}

</style>
""",
unsafe_allow_html=True
)



# Hero

st.markdown(
f"""
<div class="hero">

<h1>
Your radiology workspace
</h1>

<p>
Welcome back to <span>RadMentor</span>.
</p>

<p>
Capture clinical experiences, organize imaging knowledge,
and develop structured diagnostic reasoning.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# Quick access

st.subheader("Quick Access")


c1,c2,c3,c4 = st.columns(4)


quick = [

("Add Case",
"Document a new imaging case"),

("Library",
"Explore your cases"),

("Review",
"Strengthen memory"),

("Dashboard",
"Track learning")

]


for col,(title,text) in zip(
    [c1,c2,c3,c4],
    quick
):

    with col:

        st.markdown(
        f"""
        <div class="card">

        <h3>{title}</h3>

        <p>{text}</p>

        </div>
        """,
        unsafe_allow_html=True
        )



st.write("")


# Learning pathway

st.subheader("Your Learning Path")


st.markdown(
f"""
<div class="progress-card">

<h2>
Radiology Foundation
</h2>

<p>
Current focus: Systematic image interpretation
</p>

<p>
Progress: Getting started
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# Clinical pearl

st.subheader("Clinical Pearl")


st.markdown(
f"""
<div class="pearl">

<h3>
A systematic approach prevents missed findings.
</h3>

<p>
Always review imaging in a consistent order:
patient information, technique, anatomy,
findings, and impression.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# Recent activity

st.subheader("Recent Activity")


st.markdown(
"""
<div class="activity">

<h3>
No activity yet
</h3>

<p>
Your reviewed cases and learning progress
will appear here.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


st.markdown(
"""
<div class="footer">

<h3>
RadMentor
</h3>

<p>
Case-based radiology learning platform
</p>

</div>
""",
unsafe_allow_html=True
)
