
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


# Premium design system

st.markdown(
f"""
<style>

.main {{
    background:#f8fafc;
}}


.hero {{

    background:
    linear-gradient(135deg,#ffffff,#eef6ff);

    padding:70px 60px;

    border-radius:32px;

    border:1px solid #e2e8f0;

    box-shadow:
    0 20px 50px rgba(15,23,42,0.08);

    animation:fadeIn 1s ease;

}}


.hero h1 {{

    font-size:64px;

    font-weight:800;

    color:#0f172a;

    margin-bottom:15px;

}}


.hero span {{

    color:{accent};

}}


.hero p {{

    font-size:23px;

    color:#475569;

    max-width:850px;

    line-height:1.6;

}}


.primary-button {{

    background:{accent};

    color:white;

    padding:14px 28px;

    border-radius:14px;

    font-weight:600;

}}



.feature-card {{

    background:white;

    padding:35px;

    border-radius:24px;

    border:1px solid #e2e8f0;

    min-height:230px;

    transition:0.3s;

}}


.feature-card:hover {{

    transform:translateY(-6px);

    box-shadow:
    0 15px 35px rgba(0,0,0,0.08);

}}



.feature-title {{

    font-size:22px;

    font-weight:700;

    color:#0f172a;

}}


.feature-text {{

    color:#64748b;

    font-size:17px;

    line-height:1.6;

}}



.empty-state {{

    background:white;

    padding:45px;

    text-align:center;

    border-radius:25px;

    border:1px dashed #cbd5e1;

}}



.footer {{

    text-align:center;

    padding:40px;

    color:#64748b;

}}



@keyframes fadeIn {{

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



# Hero section

st.markdown(
f"""

<div class="hero">

<h1>
Welcome to <span>RadMentor</span>
</h1>


<p>
A personal radiology learning workspace designed
to help you capture cases, organize knowledge,
and strengthen diagnostic reasoning.
</p>


</div>

""",
unsafe_allow_html=True
)



st.write("")


# Main actions

st.subheader(
"Build your radiology knowledge"
)


col1,col2,col3 = st.columns(3)


features = [

(
"Case Library",
"Capture important imaging cases, findings, diagnoses, and teaching points in one organized workspace."
),

(
"Learning Workspace",
"Review cases, reflect on patterns, and develop a structured approach to interpretation."
),

(
"Knowledge Growth",
"Create your personal radiology memory system through continuous learning."
)

]


for col,(title,text) in zip(
    [col1,col2,col3],
    features
):

    with col:

        st.markdown(
        f"""
        <div class="feature-card">

        <div class="feature-title">
        {title}
        </div>

        <br>

        <div class="feature-text">
        {text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



st.write("")


# Empty state

st.subheader(
"Your Learning Space"
)


st.markdown(
"""
<div class="empty-state">

<h2>
No cases yet
</h2>

<p>
Your saved radiology cases will appear here.
</p>

<p>
Start by adding your first case and build your
personal imaging knowledge library.
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
Structured learning for modern radiology education

</div>
""",
unsafe_allow_html=True
)
