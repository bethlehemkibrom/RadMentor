
import streamlit as st


def clinical_pearl(pearl=None, source=None):

    if pearl is None:
        pearl = (
            "Follow a consistent search pattern to reduce perceptual errors "
            "and improve diagnostic accuracy."
        )

    if source is None:
        source = "RadMentor Knowledge Base"

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:22px;
            padding:30px;
            border-left:6px solid #2563EB;
            box-shadow:0 8px 24px rgba(0,0,0,.08);
            margin-top:25px;
        ">

        <div style="
            font-size:14px;
            color:#2563EB;
            text-transform:uppercase;
            letter-spacing:1px;
            font-weight:600;
        ">
        Clinical Pearl
        </div>

        <div style="
            font-size:22px;
            margin-top:16px;
            color:#0F172A;
            line-height:1.7;
            font-weight:500;
        ">
        "{pearl}"
        </div>

        <div style="
            margin-top:20px;
            color:#64748B;
            font-size:14px;
        ">
        Source • {source}
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
