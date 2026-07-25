
import streamlit as st


def page_header(*args):
    """
    Supports old and new usage.

    Old:
    page_header(icon, title, description)

    New:
    page_header(title, description)
    """

    if len(args) == 3:
        _, title, description = args
    elif len(args) == 2:
        title, description = args
    else:
        title = args[0]
        description = ""

    st.markdown(
        f"""
        <div style="
            padding:24px 0 16px 0;
        ">

        <h1 style="
            font-size:34px;
            font-weight:700;
            color:#111827;
            margin-bottom:8px;
        ">
        {title}
        </h1>

        <p style="
            font-size:16px;
            color:#6B7280;
        ">
        {description}
        </p>

        <hr style="
            border:none;
            border-top:1px solid #E5E7EB;
            margin-top:24px;
        ">

        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, text, *args, **kwargs):

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:16px;
            padding:22px;
            margin-bottom:18px;
        ">

        <h3 style="
            color:#111827;
            font-size:20px;
        ">
        {title}
        </h3>

        <p style="
            color:#374151;
            font-size:15px;
        ">
        {text}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


def stat_card(label, value, description=""):

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:16px;
            padding:20px;
        ">

        <div style="color:#6B7280;font-size:14px;">
        {label}
        </div>

        <div style="
            color:#111827;
            font-size:32px;
            font-weight:700;
        ">
        {value}
        </div>

        <div style="color:#6B7280;font-size:13px;">
        {description}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def section_title(title):

    st.markdown(
        f"""
        <h2 style="
            color:#111827;
            font-size:22px;
            font-weight:600;
            margin-top:30px;
        ">
        {title}
        </h2>
        """,
        unsafe_allow_html=True
    )
