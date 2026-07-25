
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color, save_accent_color
from utils.supabase_client import supabase


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
# Get user
# --------------------

user = st.session_state.get(
    "user",
    None
)



# --------------------
# Load cases
# --------------------

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



# --------------------
# CSS
# --------------------

st.markdown(
f"""
<style>

.hero {{

background:
linear-gradient(135deg,#ffffff,#eff6ff);

padding:60px;

border-radius:35px;

border:1px solid #dbeafe;

box-shadow:
0 20px 45px rgba(15,23,42,.08);

}}


.hero h1 {{

font-size:58px;

color:#0f172a;

}}


.hero span {{

color:{accent};

}}


.hero p {{

font-size:22px;

color:#475569;

}}



.card {{

background:white;

padding:30px;

border-radius:24px;

border:1px solid #e2e8f0;

box-shadow:
0 8px 25px rgba(0,0,0,.05);

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

border-radius:25px;

background:white;

border:1px dashed #cbd5e1;

}}


</style>
""",
unsafe_allow_html=True
)



# --------------------
# Header
# --------------------

if user:

    st.markdown(
    f"""
    <div class="hero">

    <h1>
    Welcome back
    </h1>

    <p>
    Your personal radiology learning workspace.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

else:

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
    Capture cases, organize imaging knowledge,
    and develop stronger diagnostic reasoning.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")



# --------------------
# Logged in dashboard
# --------------------

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

        Cases collected

        </div>
        """,
        unsafe_allow_html=True
        )


    with c2:

        modalities = len(
            set(
                [
                    c.get(
                        "modality"
                    )
                    for c in cases
                ]
            )
        ) if cases else 0


        st.markdown(
        f"""
        <div class="card">

        <div class="metric">
        {modalities}
        </div>

        </div>

        Imaging modalities

        """,
        unsafe_allow_html=True
        )


    with c3:

        st.markdown(
        f"""
        <div class="card">

        <div class="metric">
        Ready
        </div>

        Continue learning

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


        for col,case in zip(
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
        Add your first radiology case
        to begin building your knowledge base.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


# --------------------
# Public landing
# --------------------

else:


    st.subheader(
        "How RadMentor helps"
    )


    a,b,c = st.columns(3)


    for col,title,text in zip(
        [a,b,c],
        [
            (
            "Capture",
            "Save important imaging cases."
            ),
            (
            "Review",
            "Strengthen diagnostic patterns."
            ),
            (
            "Improve",
            "Build your radiology memory."
            )
        ]
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
