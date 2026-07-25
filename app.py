
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


# Premium CSS

st.markdown(
f"""
<style>

.hero {{
background:
linear-gradient(135deg,#ffffff,#eff6ff);

border-radius:30px;

padding:45px;

border:1px solid #e2e8f0;

box-shadow:
0 15px 40px rgba(15,23,42,0.08);

}}


.hero h1 {{
font-size:55px;
color:{accent};
margin-bottom:10px;
}}


.hero p {{
font-size:22px;
color:#475569;
}}


.stat-card {{
background:white;

padding:25px;

border-radius:22px;

border:1px solid #e2e8f0;

box-shadow:
0 8px 25px rgba(0,0,0,0.05);

}}


.stat-number {{
font-size:42px;
font-weight:800;
color:{accent};
}}


.stat-title {{
font-size:18px;
color:#475569;
}}


.learning-card {{

background:
linear-gradient(135deg,#2563eb,#1d4ed8);

color:white;

padding:30px;

border-radius:25px;

}}


.case-card {{

background:white;

border-radius:20px;

padding:25px;

border:1px solid #e2e8f0;

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
🩻 RadMentor
</h1>

<p>
Your personal radiology intelligence workspace.
</p>

<p>
Transform every image into knowledge.
Build diagnostic confidence through
case-based learning.
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")


# Stats

st.subheader("Your Radiology Journey")


c1,c2,c3,c4 = st.columns(4)


stats=[
("24","Cases"),
("12","Reviews"),
("7","Day streak"),
("86%","Progress")
]


for col,(number,title) in zip(
    [c1,c2,c3,c4],
    stats
):

    with col:

        st.markdown(
        f"""
        <div class="stat-card">

        <div class="stat-number">
        {number}
        </div>

        <div class="stat-title">
        {title}
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )


st.write("")


# Learning focus

st.subheader("Today's Learning")


st.markdown(
"""
<div class="learning-card">

<h2>
Chest X-Ray Interpretation
</h2>

<p>
Focus: Systematic approach to chest imaging
</p>

<p>
Difficulty: Intermediate
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# Recent cases

st.subheader("Recent Cases")


c1,c2,c3 = st.columns(3)


cases=[
("Chest X-Ray","Pleural effusion"),
("CT Brain","Acute hemorrhage"),
("Ultrasound","Gallstones")
]


for col,(modality,diagnosis) in zip(
    [c1,c2,c3],
    cases
):

    with col:

        st.markdown(
        f"""
        <div class="case-card">

        <h3>
        {modality}
        </h3>

        <p>
        {diagnosis}
        </p>

        <small>
        Review case →
        </small>

        </div>
        """,
        unsafe_allow_html=True
        )



st.write("")


st.markdown(
f"""
<div class="hero">

<h2 style="color:{accent}">
Keep learning. Keep improving.
</h2>

<p>
Every case reviewed is a step toward diagnostic mastery.
</p>

</div>
""",
unsafe_allow_html=True
)
