
import streamlit as st

def today_focus():

    st.markdown(
        """
        <div style="
            background:linear-gradient(135deg,#0F172A,#1E3A8A);
            color:white;
            border-radius:22px;
            padding:30px;
            margin-top:25px;
            margin-bottom:25px;
            box-shadow:0 10px 30px rgba(0,0,0,.15);
        ">

        <div style="
            font-size:14px;
            opacity:.8;
            text-transform:uppercase;
            letter-spacing:1px;
        ">
        Today's Focus
        </div>

        <div style="
            font-size:30px;
            font-weight:700;
            margin-top:10px;
        ">
        Chest CT Interpretation
        </div>

        <div style="
            margin-top:12px;
            font-size:17px;
            opacity:.85;
        ">
        Recommended review time: 15 minutes
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "Start Learning Session",
        use_container_width=True,
        type="primary"
    )
