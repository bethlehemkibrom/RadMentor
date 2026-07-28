
import streamlit as st
from components.dashboard import dashboard

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color
from utils.supabase_client import supabase


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


# User

user = st.session_state.get("user", None)


# Load cases

cases = []

if user and supabase:

    try:

        response = (
            supabase
            .table("cases")
            .select("*")
            .eq("user_id", user.id)
            .order(
                "created_at",
                desc=True
            )
            .execute()
        )

        cases = response.data or []

    except Exception:

        cases = []



# CSS

st.markdown(
f"""
<style>

.hero {{
background:linear-gradient(135deg,#ffffff,#eff6ff);
padding:60px;
border-radius:35px;
border:1px solid #dbeafe;
box-shadow:0 20px 45px rgba(15,23,42,.08);
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
line-height:1.6;
}}

.card {{
background:white;
padding:30px;
border-radius:24px;
border:1px solid #e2e8f0;
box-shadow:0 8px 25px rgba(0,0,0,.05);
min-height:180px;
}}

.card h3 {{
color:{accent};
}}

.metric {{
font-size:42px;
font-weight:800;
color:{accent};
}}

.case-card {{
background:#f8fafc;
padding:25px;
border-radius:20px;
border:1px solid #e2e8f0;
}}

.empty {{
padding:40px;
text-align:center;
background:white;
border-radius:25px;
border:1px dashed #cbd5e1;
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

if user:

    dashboard(user)

    st.stop()

else:

    title = "Your radiology <span>learning workspace</span>"
    subtitle = (
        "Capture cases, organize imaging knowledge, "
        "and develop stronger diagnostic reasoning."
    )


st.markdown(
f"""
<div class="hero">

<h1>
{title}
</h1>

<p>
{subtitle}
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")



# Dashboard for logged in users

if user:

    st.subheader(
        "Your Imaging Knowledge Base"
    )


    c1,c2,c3 = st.columns(3)


    with c1:

        st.markdown(
        f"""
        <div class="card">

        <div class="metric">
        {len(cases)}
        </div>

        <p>
        Cases collected
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with c2:

        modality_count = len(
            set(
                case.get("modality")
                for case in cases
                if case.get("modality")
            )
        )

        st.markdown(
        f"""
        <div class="card">

        <div class="metric">
        {modality_count}
        </div>

        <p>
        Modalities
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with c3:

        st.markdown(
        """
        <div class="card">

        <div class="metric">
        Active
        </div>

        <p>
        Learning journey
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    st.write("")


    st.subheader(
        "Recent Cases"
    )


    if cases:

        cols = st.columns(3)

        for col, case in zip(
            cols,
            cases[:3]
        ):

            with col:

                st.markdown(
                f"""
                <div class="case-card">

                <h3>
                {case.get("modality","")}
                </h3>

                <p>
                {case.get("diagnosis","No diagnosis")}
                </p>

                </div>
                """,
                unsafe_allow_html=True
                )

    else:

        st.markdown(
        """
        <div class="empty">

        <h2>
        No cases yet
        </h2>

        <p>
        Start adding cases to build your
        personal radiology knowledge base.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



# Public landing page

else:

    st.subheader(
        "How RadMentor helps"
    )


    features = [
        (
            "Capture Cases",
            "Document imaging findings and clinical lessons."
        ),
        (
            "Review Knowledge",
            "Strengthen diagnostic reasoning through repetition."
        ),
        (
            "Build Expertise",
            "Create your personal radiology learning system."
        )
    ]


    cols = st.columns(3)


    for col, feature in zip(
        cols,
        features
    ):

        title, text = feature

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
