
import streamlit as st


def quick_actions():

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
        Quick Actions
        </div>
        """,
        unsafe_allow_html=True,
    )


    c1, c2, c3 = st.columns(3)


    with c1:
        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                text-align:center;
                border:1px solid #E5E7EB;
                box-shadow:0 5px 15px rgba(0,0,0,.05);
            ">
            <h3>Add Case</h3>
            <p style="color:#64748B">
            Document a new radiology case
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with c2:
        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                text-align:center;
                border:1px solid #E5E7EB;
                box-shadow:0 5px 15px rgba(0,0,0,.05);
            ">
            <h3>Review Queue</h3>
            <p style="color:#64748B">
            Continue your learning review
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with c3:
        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                text-align:center;
                border:1px solid #E5E7EB;
                box-shadow:0 5px 15px rgba(0,0,0,.05);
            ">
            <h3>Case Library</h3>
            <p style="color:#64748B">
            Explore your knowledge archive
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
