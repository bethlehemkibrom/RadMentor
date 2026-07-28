
import streamlit as st


def activity_feed(activities=None):

    if not activities:
        activities = [
            "No recent cases yet. Start building your radiology library."
        ]

    st.markdown(
        """
        <div style="
            font-size:14px;
            color:#2563EB;
            text-transform:uppercase;
            letter-spacing:1px;
            font-weight:600;
            margin-top:30px;
            margin-bottom:15px;
        ">
        Recent Activity
        </div>
        """,
        unsafe_allow_html=True,
    )


    for item in activities:

        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:20px;
                margin-bottom:12px;
                border:1px solid #E5E7EB;
                box-shadow:0 5px 15px rgba(0,0,0,.05);
            ">

            <div style="
                color:#0F172A;
                font-size:17px;
                font-weight:500;
            ">
            {item}
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )
