
import streamlit as st


def growth_chart():

    st.markdown(
        """
        <div style="
            font-size:14px;
            color:#2563EB;
            text-transform:uppercase;
            letter-spacing:1px;
            font-weight:600;
            margin-top:35px;
            margin-bottom:15px;
        ">
        Radiology Growth
        </div>
        """,
        unsafe_allow_html=True,
    )


    c1, c2 = st.columns(2)


    with c1:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:20px;
                padding:25px;
                border:1px solid #E5E7EB;
                box-shadow:0 6px 18px rgba(0,0,0,.06);
            ">

            <h3 style="color:#0F172A;">
            Learning Progress
            </h3>

            <p>MRI Interpretation</p>

            <div style="
                background:#E2E8F0;
                border-radius:10px;
                height:12px;
            ">
                <div style="
                    background:#2563EB;
                    width:80%;
                    height:12px;
                    border-radius:10px;
                "></div>
            </div>

            <p style="margin-top:15px;">
            CT Interpretation
            </p>

            <div style="
                background:#E2E8F0;
                border-radius:10px;
                height:12px;
            ">
                <div style="
                    background:#2563EB;
                    width:65%;
                    height:12px;
                    border-radius:10px;
                "></div>
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    with c2:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:20px;
                padding:25px;
                border:1px solid #E5E7EB;
                box-shadow:0 6px 18px rgba(0,0,0,.06);
            ">

            <h3 style="color:#0F172A;">
            Learning Activity
            </h3>

            <h1 style="
                color:#1E3A8A;
                margin-bottom:5px;
            ">
            7
            </h1>

            <p style="color:#64748B;">
            Day learning streak
            </p>

            <hr>

            <h2 style="
                color:#1E3A8A;
            ">
            24
            </h2>

            <p style="color:#64748B;">
            Cases reviewed
            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )
