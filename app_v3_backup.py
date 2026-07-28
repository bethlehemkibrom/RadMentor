
import streamlit as st
import os

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


# CSS

st.markdown(
f"""
<style>

.hero {{

background:
linear-gradient(120deg,#ffffff,#eef5ff);

padding:70px;

border-radius:35px;

border:1px solid #dbeafe;

box-shadow:
0 20px 50px rgba(15,23,42,0.08);

}}


.hero h1 {{

font-size:64px;

font-weight:800;

color:#0f172a;

}}


.hero h1 span {{

color:{accent};

}}


.hero p {{

font-size:22px;

color:#475569;

line-height:1.6;

max-width:850px;

}}



.image-box {{

height:260px;

background:
linear-gradient(135deg,#e0f2fe,#dbeafe);

border-radius:30px;

display:flex;

align-items:center;

justify-content:center;

font-size:22px;

color:#334155;

}}



.card {{

background:white;

padding:35px;

border-radius:25px;

border:1px solid #e2e8f0;

height:220px;

box-shadow:
0 10px 30px rgba(0,0,0,0.05);

transition:0.3s;

}}


.card:hover {{

transform:translateY(-5px);

}}



.card h3 {{

color:{accent};

}}



.empty {{

background:#ffffff;

border-radius:25px;

padding:45px;

border:1px dashed #cbd5e1;

text-align:center;

}}


.footer {{

text-align:center;

padding:40px;

color:#64748b;

}}

</style>
""",
unsafe_allow_html=True
)



# Hero

left,right = st.columns([1.3,0.7])


with left:

    st.markdown(
    f"""
    <div class="hero">

    <h1>
    Your radiology
    <span>
    learning workspace
    </span>
    </h1>


    <p>
    Capture clinical cases, organize imaging knowledge,
    and develop stronger diagnostic reasoning through
    structured learning.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


with right:

    st.markdown(
    """
    <div class="image-box">

    Radiology Workspace

    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")


# Buttons

st.subheader("Get started")


b1,b2,b3 = st.columns(3)


with b1:

    if st.button("Add a Case",use_container_width=True):
        st.switch_page("pages/1_Add_Case.py")


with b2:

    if st.button("Explore Cases",use_container_width=True):
        st.switch_page("pages/2_Case_Library.py")


with b3:

    if st.button("Learning Dashboard",use_container_width=True):
        st.switch_page("pages/3_Learning_Dashboard.py")



st.write("")


# How it works

st.subheader("How RadMentor works")


c1,c2,c3 = st.columns(3)


steps=[

("Capture",
"Save important imaging cases and clinical lessons."),

("Review",
"Return to cases and strengthen pattern recognition."),

("Improve",
"Build a personal radiology knowledge system.")

]


for col,(title,text) in zip(
    [c1,c2,c3],
    steps
):

    with col:

        st.markdown(
        f"""
        <div class="card">

        <h3>{title}</h3>

        <p>
        {text}
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



st.write("")


# Learning space

st.subheader("Your Learning Space")


st.markdown(
"""
<div class="empty">

<h2>
Start building your library
</h2>

<p>
Your saved radiology cases will appear here.
</p>

<p>
Every case becomes part of your personal diagnostic memory.
</p>

</div>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="footer">

RadMentor

<br>

Structured radiology learning platform

</div>
""",
unsafe_allow_html=True
)
