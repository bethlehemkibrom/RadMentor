
import streamlit as st

from utils.supabase_client import supabase
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state


apply_theme(get_accent_color())


page_header(
    "📝",
    "Edit Case",
    "Update and improve your radiology learning cases."
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



if not cases:

    empty_state(
        "No cases available to edit."
    )

    st.stop()



case_names = [

    f"{i+1}. {c.get('diagnosis','Unknown')}"

    for i, c in enumerate(cases)

]


selected = st.selectbox(
    "Choose case",
    case_names
)


index = case_names.index(selected)

case = cases[index]



diagnosis = st.text_input(
    "Diagnosis",
    case.get("diagnosis","")
)


clinical_history = st.text_area(
    "Clinical History",
    case.get("clinical_history","")
)


findings = st.text_area(
    "Imaging Findings",
    case.get("findings","")
)


differential = st.text_area(
    "Differential Diagnosis",
    case.get("differential","")
)


notes = st.text_area(
    "Teaching Pearls",
    case.get("notes","")
)


learning_points = st.text_area(
    "Learning Points",
    case.get("learning_points","")
)



if st.button(
    "💾 Save Changes",
    type="primary"
):

    updated = {

        "diagnosis": diagnosis,
        "clinical_history": clinical_history,
        "findings": findings,
        "differential": differential,
        "notes": notes,
        "learning_points": learning_points,

    }


    try:

        (
            supabase
            .table("cases")
            .update(updated)
            .eq(
                "id",
                case["id"]
            )
            .execute()
        )


        st.success(
            "Case updated successfully ✅"
        )


    except Exception as e:

        st.error(
            "Update failed"
        )
