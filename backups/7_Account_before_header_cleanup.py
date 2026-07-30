
import streamlit as st

from utils.supabase_client import supabase


st.set_page_config(
    page_title="Account | RadMentor",
    page_icon="🩻"
)


if "user" not in st.session_state:
    st.session_state.user = None

if "show_reset" not in st.session_state:
    st.session_state.show_reset = False


st.title("RadMentor Account")


email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)


if st.button("Create Account"):

    if supabase is None:
        st.error("Supabase is not connected.")

    else:
        try:
            supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password
                }
            )

            st.success("Account created successfully.")

        except Exception:
            st.warning(
                "Unable to create account."
            )


if st.button("Login"):

    if supabase is None:

        st.error(
            "Supabase is not connected."
        )

    else:

        try:

            response = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password
                }
            )

            st.session_state.user = response.user
            st.session_state.show_reset = False

            st.success(
                "Welcome to RadMentor"
            )


        except Exception:

            st.session_state.show_reset = True

            st.warning(
                "Incorrect email or password."
            )


if st.session_state.show_reset:

    if st.button("Forgot password?"):

        if not email:

            st.warning(
                "Please enter your email first."
            )

        else:

            try:

                supabase.auth.reset_password_email(
                    email
                )

                st.success(
                    "Password reset link sent. Check your email."
                )

            except Exception:

                st.warning(
                    "Unable to send reset email."
                )


if st.session_state.user:

    st.info(
        f"Logged in as: {st.session_state.user.email}"
    )
