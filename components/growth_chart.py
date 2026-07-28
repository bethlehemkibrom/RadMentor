
import streamlit as st


def growth_chart(stats=None):

    if stats is None:
        stats = {}

    reviewed = stats.get("reviewed", 0)
    pending = stats.get("pending", 0)

    modalities = stats.get(
        "modalities",
        {}
    )

    top_modality = "None"

    if modalities:
        top_modality = max(
            modalities,
            key=modalities.get
        )


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


    c1, c2, c3 = st.columns(3)


    with c1:
        st.metric(
            "Cases Reviewed",
            reviewed
        )


    with c2:
        st.metric(
            "Pending Review",
            pending
        )


    with c3:
        st.metric(
            "Most Studied Modality",
            top_modality
        )
