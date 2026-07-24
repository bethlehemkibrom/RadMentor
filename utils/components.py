
import streamlit as st


def page_header(icon, title, description):

    st.markdown(
        f"""
        ## {icon} {title}

        {description}

        ---
        """
    )


def info_card(title, text, icon="🩻"):

    st.markdown(
        f"""
        <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        margin-bottom:15px;
        ">

        <h3>{icon} {title}</h3>

        <p>{text}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


def empty_state(message):

    st.info(message)
