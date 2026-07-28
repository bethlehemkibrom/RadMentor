
import streamlit as st
from utils.supabase_client import supabase


st.set_page_config(
    page_title="Case Library | RadMentor",
    page_icon="🩻",
    layout="wide"
)


st.title("Case Library")
st.caption(
    "Explore, review, and organize your radiology learning cases."
)


if "user" not in st.session_state or st.session_state.user is None:

    st.warning(
        "Please login first from the Account page."
    )

    st.stop()


user = st.session_state.user


# Load cases

cases = []

if supabase:

    try:

        response = (
            supabase
            .table("cases")
            .select("*")
            .eq(
                "user_id",
                user.id
            )
            .order(
                "created_at",
                desc=True
            )
            .execute()
        )

        cases = response.data or []

    except Exception:

        cases = []


# Search and filters

col1, col2, col3 = st.columns(3)


with col1:

    search = st.text_input(
        "Search diagnosis"
    )


with col2:

    modalities = sorted(
        list(
            set(
                c.get("modality")
                for c in cases
                if c.get("modality")
            )
        )
    )

    modality_filter = st.selectbox(
        "Modality",
        ["All"] + modalities
    )


with col3:

    statuses = sorted(
        list(
            set(
                c.get("review_status")
                for c in cases
                if c.get("review_status")
            )
        )
    )

    status_filter = st.selectbox(
        "Review Status",
        ["All"] + statuses
    )


st.divider()


# Filter cases

filtered_cases = cases


if search:

    filtered_cases = [
        c for c in filtered_cases
        if search.lower()
        in c.get(
            "diagnosis",
            ""
        ).lower()
    ]


if modality_filter != "All":

    filtered_cases = [
        c for c in filtered_cases
        if c.get("modality") == modality_filter
    ]


if status_filter != "All":

    filtered_cases = [
        c for c in filtered_cases
        if c.get("review_status") == status_filter
    ]



if not filtered_cases:

    st.info(
        "No cases found. Add your first radiology case."
    )

    st.stop()



st.subheader(
    f"{len(filtered_cases)} Cases"
)



for case in filtered_cases:

    with st.container():

        st.markdown(
            """
            <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            border:1px solid #E2E8F0;
            box-shadow:0 5px 18px rgba(0,0,0,.05);
            ">
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"### {case.get('diagnosis','Unnamed Case')}"
        )


        st.write(
            f"**Modality:** {case.get('modality','-')}"
        )

        st.write(
            f"**Body System:** {case.get('body_system','-')}"
        )

        st.write(
            f"**Status:** {case.get('review_status','Not reviewed')}"
        )


        if case.get("teaching_pearls"):

            st.info(
                case["teaching_pearls"]
            )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.write("")
