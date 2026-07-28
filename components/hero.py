
import streamlit as st


def hero(user=None):

    if user:
        greeting = f"""
        <h1 style='margin-bottom:0'>
        Welcome back
        </h1>

        <h2 style='margin-top:5px;color:#2563eb'>
        {user.email}
        </h2>

        <p style='font-size:20px;color:#64748b'>
        Your Radiology Learning Workspace
        </p>
        """

    else:
        greeting = """
        <h1 style='margin-bottom:0'>
        RadMentor
        </h1>

        <h2 style='margin-top:5px;color:#2563eb'>
        Radiology Learning Workspace
        </h2>

        <p style='font-size:20px;color:#64748b'>
        Capture • Learn • Review • Master
        </p>
        """

    st.markdown(
        f"""
        <div style="
            padding:55px;
            border-radius:30px;
            background:linear-gradient(135deg,#ffffff,#eef6ff);
            border:1px solid #dbeafe;
            box-shadow:0 12px 35px rgba(0,0,0,.06);
        ">
            {greeting}
        </div>
        """,
        unsafe_allow_html=True
    )
