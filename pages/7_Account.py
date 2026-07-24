
import streamlit as st

from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.supabase_client import supabase


apply_theme(get_accent_color())


st.title("🔐 RadMentor Account")


email = st.text_input(
    "Email"
)


password = st.text_input(
    "Password",
    type="password"
)



if "user" not in st.session_state:
    st.session_state.user = None



if st.button("Create Account"):


    if supabase is None:

        st.error(
            "Supabase is not connected."
        )

    else:

        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password
            }
        )

        st.success(
            "Account created. Check email verification if required."
        )



if st.button("Login"):


    if supabase is None:

        st.error(
            "Supabase is not connected."
        )

    else:

        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )


        st.session_state.user = (
            response.user
        )


        st.success(
            "Welcome to RadMentor 🩻"
        )



if st.session_state.user:

    st.info(
        f"Logged in as: {st.session_state.user.email}"
    )


    if st.button("Logout"):

        supabase.auth.sign_out()

        st.session_state.user = None

        st.rerun()
