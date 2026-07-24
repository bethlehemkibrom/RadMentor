
import streamlit as st

from utils.storage import load_cases
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state, info_card


apply_theme(get_accent_color())


page_header(
    "🔁",
    "Review Queue",
    "Revisit important cases and strengthen your radiology memory."
)


cases = load_cases()


review_cases = [

    case for case in cases

    if case.get(
        "review_status",
        "Not reviewed"
    ) == "Not reviewed"

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


else:


    st.write(
        f"{len(review_cases)} cases need attention"
    )



    for case in review_cases:


        st.subheader(
            f"⭐ {case.get('diagnosis','Unknown')}"
        )


        st.write(
            f"**Priority:** {case.get('priority','Normal')}"
        )


        st.write(
            f"**Status:** {case.get('review_status','Not reviewed')}"
        )


        st.write(
            f"**Modality:** {case.get('modality','')}"
        )


        info_card(
            "💡 Teaching Pearl",
            case.get(
                "notes",
                "No notes available."
            )
        )



        if case.get("reference_link"):


            st.subheader(
                "🔗 Review Resource"
            )


            st.write(
                case.get(
                    "reference_title",
                    "External resource"
                )
            )


            st.markdown(
                f"[Open Resource]({case['reference_link']})"
            )



        st.divider()
