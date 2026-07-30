
import streamlit as st

from utils.supabase_client import supabase
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state


apply_theme(get_accent_color())


page_header(
    "🔁",
    "Review Queue",
    "Revisit important cases and strengthen your radiology memory."
)


if "user" not in st.session_state or st.session_state.user is None:

    st.warning(
        "Please login first from the Account page."
    )

    st.stop()


user = st.session_state.user


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



review_cases = [

    case for case in cases

    if case.get(
        "review_status",
        "Not reviewed"
    ) != "Reviewed"

    or case.get(
        "priority",
        "Normal"
    ) in [
        "Important",
        "Must review"
    ]

]



if not review_cases:

    empty_state(
        "No cases waiting for review 🎉"
    )

    st.stop()



st.subheader(
    f"{len(review_cases)} Cases Need Attention"
)



for case in review_cases:

    with st.container():

        st.markdown(
            f"""
            <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            border:1px solid #E2E8F0;
            box-shadow:0 5px 18px rgba(0,0,0,.05);
            ">
            
            <h3>
            {case.get('diagnosis','Unknown Diagnosis')}
            </h3>

            <p>
            <b>Modality:</b> {case.get('modality','-')}
            </p>

            <p>
            <b>Body System:</b> {case.get('body_system','-')}
            </p>

            <p>
            <b>Priority:</b> {case.get('priority','Normal')}
            </p>

            <p>
            <b>Status:</b> {case.get('review_status','Not reviewed')}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        if case.get("teaching_pearls"):

            st.info(
                case["teaching_pearls"]
            )


        if case.get("reference_link"):

            st.markdown(
                f"[Open Reference]({case['reference_link']})"
            )


        st.divider()
