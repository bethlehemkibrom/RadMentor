
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


# Design

st.markdown(
f"""
<style>

.hero {{

background:
linear-gradient(135deg,#ffffff,#eff6ff);

padding:55px;

border-radius:30px;

border:1px solid #e2e8f0;

box-shadow:
0 15px 40px rgba(15,23,42,0.08);

text-align:center;

}}


.hero h1 {{

font-size:60px;

color:{accent};

}}


.hero p {{

font-size:22px;

color:#475569;

line-height:1.6;

}}


.action-card {{

background:white;

padding:30px;

border-radius:24px;

border:1px solid #e2e8f0;

box-shadow:
0 8px 25px rgba(0,0,0,0.05);

min-height:220px;

}}


.action-card h3 {{

color:{accent};

}}


.empty-card {{

background:#f8fafc;

padding:35px;

border-radius:25px;

text-align:center;

border:1px dashed #cbd5e1;

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
Your personal radiology learning workspace.
</p>

<p>
Capture cases, reflect on findings,
and build diagnostic confidence
one image at a time.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


st.subheader(
"Start Your Radiology Journey"
)


c1,c2,c3 = st.columns(3)


items = [

(
"🩻 Capture Cases",
"Save important imaging cases, diagnoses, and teaching points."
),

(
"📚 Review & Learn",
"Return to cases and strengthen your diagnostic reasoning."
),

(
"📊 Track Growth",
"Build a personal record of your learning journey."
)

]


for col,(title,text) in zip(
    [c1,c2,c3],
    items
):

    with col:

        st.markdown(
        f"""
        <div class="action-card">

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


st.subheader(
"Your Case Library"
)


st.markdown(
"""
<div class="empty-card">

<h2>
No cases yet
</h2>

<p>
Your saved radiology cases will appear here.
</p>

<p>
Start by adding your first teaching case.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


st.markdown(
f"""
<div class="hero">

<h2 style="color:{accent}">
Every image is a learning opportunity.
</h2>

<p>
RadMentor helps you transform clinical exposure
into lasting radiology knowledge.
</p>

</div>
""",
unsafe_allow_html=True
)
