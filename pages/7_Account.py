
import streamlit as st

from utils.supabase_client import supabase


st.set_page_config(
    page_title="Account | RadMentor",
    page_icon="🩻"
)


if "user" not in st.session_state:
    st.session_state.user = None


st.title("RadMentor Account")


email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)


# Create account

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

            st.success(
                "Account created successfully."
            )

        except Exception:

            st.warning(
                "Unable to create account. Please check your details."
            )


# Login

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


            st.success(
                "Welcome to RadMentor"
            )


        except Exception:

            st.warning(
                "Incorrect email or password. Please try again."
            )


# Forgot password

st.divider()

st.subheader("Password recovery")


reset_email = st.text_input(
    "Enter your email to reset password",
    key="reset_email"
)


if st.button("Send Password Reset Link"):

    if supabase is None:

        st.error(
            "Supabase is not connected."
        )

    else:

        try:

            supabase.auth.reset_password_email(
                reset_email
            )

            st.success(
                "Password reset link sent. Check your email."
            )


        except Exception:

            st.warning(
                "Unable to send reset link. Check your email address."
            )


# Logged in user

if st.session_state.user:

    st.info(
        f"Logged in as: {st.session_state.user.email}"
    )
