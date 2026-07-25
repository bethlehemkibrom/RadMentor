
import streamlit as st


def page_header(*args):

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
            padding:24px 0;
        ">
        <h1 style="
            color:#111827;
            font-size:34px;
            font-weight:700;
        ">
        {title}
        </h1>

        <p style="
            color:#6B7280;
            font-size:16px;
        ">
        {description}
        </p>

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

        <h3 style="color:#111827;">
        {title}
        </h3>

        <p style="color:#374151;">
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

        <p style="color:#6B7280;">
        {label}
        </p>

        <h2 style="color:#111827;">
        {value}
        </h2>

        <small style="color:#6B7280;">
        {description}
        </small>

        </div>
        """,
        unsafe_allow_html=True
    )


def section_title(title):

    st.markdown(
        f"""
        <h2 style="
            color:#111827;
            margin-top:30px;
        ">
        {title}
        </h2>
        """,
        unsafe_allow_html=True
    )


def empty_state(title, message=""):

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px dashed #CBD5E1;
            border-radius:16px;
            padding:30px;
            text-align:center;
        ">

        <h3 style="color:#111827;">
        {title}
        </h3>

        <p style="color:#6B7280;">
        {message}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
