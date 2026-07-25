
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color


st.set_page_config(
    page_title="RadMentor",
    page_icon="R",
    layout="wide"
)


# --------------------
# Theme
# --------------------

current_color = get_accent_color()

accent = st.sidebar.color_picker(
    "Accent colour",
    current_color
)

if accent != current_color:
    save_accent_color(accent)
    st.rerun()


apply_theme(accent)


# --------------------
# Design system
# --------------------

st.markdown(
f"""
<style>

body {{
font-family: Inter, sans-serif;
}}


.hero {{

background:
linear-gradient(135deg,#ffffff,#f0f7ff);

padding:65px;

border-radius:35px;

border:1px solid #dbeafe;

box-shadow:
0 20px 50px rgba(15,23,42,.08);

}}


.hero h1 {{

font-size:58px;

font-weight:800;

color:#0f172a;

}}


.hero span {{

color:{accent};

}}


.hero p {{

font-size:22px;

color:#475569;

line-height:1.7;

max-width:850px;

}}



.section-card {{

background:white;

padding:32px;

border-radius:24px;

border:1px solid #e2e8f0;

box-shadow:
0 10px 30px rgba(0,0,0,.05);

height:220px;

transition:.3s;

}}


.section-card:hover {{

transform:translateY(-5px);

}}



.section-card h3 {{

color:{accent};

font-size:24px;

}}



.learning {{

background:
linear-gradient(135deg,{accent},#1e40af);

color:white;

padding:35px;

border-radius:28px;

}}



.learning h2 {{

color:white;

}}



.case {{

background:#f8fafc;

padding:35px;

border-radius:25px;

border:1px solid #e2e8f0;

}}



.empty {{

text-align:center;

padding:45px;

background:white;

border-radius:25px;

border:1px dashed #cbd5e1;

}}



.footer {{

text-align:center;

padding:50px;

color:#64748b;

}}



.fade {{

animation:fade 1s ease;

}}



@keyframes fade {{

from {{
opacity:0;
transform:translateY(20px);
}}

to {{
opacity:1;
transform:translateY(0);
}}

}}

</style>
""",
unsafe_allow_html=True
)



# --------------------
# Hero
# --------------------

st.markdown(
f"""
<div class="hero fade">

<h1>
Welcome to <span>RadMentor</span>
</h1>

<p>
A case-based radiology learning platform designed
to help you capture clinical experiences,
organize imaging knowledge, and develop stronger
diagnostic reasoning.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# --------------------
# Quick actions
# --------------------

st.subheader("Your Workspace")


a,b,c = st.columns(3)


actions = [

(
"Add Cases",
"Document important imaging cases and create your personal teaching archive."
),

(
"Review Library",
"Return to previous cases and strengthen recognition of imaging patterns."
),

(
"Learning Dashboard",
"Follow your progress and build structured radiology knowledge."
)

]


for col,(title,text) in zip(
[a,b,c],
actions
):

    with col:

        st.markdown(
        f"""
        <div class="section-card">

        <h3>{title}</h3>

        <p>{text}</p>

        </div>
        """,
        unsafe_allow_html=True
        )



st.write("")


# --------------------
# Learning focus
# --------------------

st.subheader("Today's Learning Focus")


st.markdown(
"""
<div class="learning">

<h2>
Chest X-ray Systematic Interpretation
</h2>

<p>
Recommended activity:
Review a structured approach to chest imaging.
</p>

<p>
Estimated learning time: 10 minutes
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# --------------------
# Case of the day
# --------------------

st.subheader("Case of the Day")


st.markdown(
"""
<div class="case">

<h2>
No featured case yet
</h2>

<p>
A curated teaching case will appear here.
</p>

<p>
Each case will help you connect imaging findings
with clinical reasoning.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")


# --------------------
# Empty library
# --------------------

st.subheader("Your Case Library")


st.markdown(
"""
<div class="empty">

<h2>
Start building your radiology library
</h2>

<p>
Your saved cases, reflections, and learning notes
will appear here.
</p>

</div>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="footer">

<h3>
RadMentor
</h3>

<p>
Case-based learning for modern radiology education
</p>

</div>
""",
unsafe_allow_html=True
)
