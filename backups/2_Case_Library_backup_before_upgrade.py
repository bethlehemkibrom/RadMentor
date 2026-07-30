
import streamlit as st

from utils.storage import load_cases, save_cases
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, info_card, empty_state


apply_theme(get_accent_color())


page_header(
    "📚",
    "Case Library",
    "Review, organize, and manage your radiology cases."
)


cases = load_cases()


if not cases:

    empty_state(
        "No cases saved yet."
    )


else:


    search = st.text_input(
        "🔎 Search cases"
    )


    for index, case in enumerate(cases):


        searchable = (
            case.get("diagnosis","")
            + case.get("clinical_history","")
            + case.get("findings","")
            + case.get("notes","")
        ).lower()



        if search.lower() not in searchable:
            continue



        st.subheader(
            f"🩻 {case.get('diagnosis','Unknown')}"
        )


        st.write(
            f"**Status:** {case.get('review_status','Not reviewed')}"
        )


        st.write(
            f"**Priority:** {case.get('priority','Normal')}"
        )


        st.write(
            f"**Modality:** {case.get('modality','')}"
        )



        info_card(
            "🧑‍⚕️ Clinical History",
            case.get("clinical_history","")
        )


        info_card(
            "🔍 Imaging Findings",
            case.get("findings","")
        )


        info_card(
            "💡 Teaching Pearls",
            case.get("notes","")
        )



        if case.get("reference_link"):

            st.markdown(
                f"[🔗 Open Resource]({case['reference_link']})"
            )



        if case.get("image_path"):

            st.image(
                case["image_path"],
                caption="Case Image"
            )



        col1, col2, col3 = st.columns(3)



        with col1:

            if st.button(
                "✅ Reviewed",
                key=f"review_{index}"
            ):

                cases[index]["review_status"] = "Reviewed"

                save_cases(cases)

                st.success(
                    "Marked as reviewed"
                )

                st.rerun()



        with col2:

            priority = st.selectbox(
                "⭐ Priority",
                [
                    "Normal",
                    "Important",
                    "Must review"
                ],
                index=[
                    "Normal",
                    "Important",
                    "Must review"
                ].index(
                    case.get(
                        "priority",
                        "Normal"
                    )
                ),
                key=f"priority_{index}"
            )


            if priority != case.get("priority"):

                cases[index]["priority"] = priority

                save_cases(cases)

                st.rerun()



        with col3:

            if st.button(
                "🗑️ Delete",
                key=f"delete_{index}"
            ):

                cases.pop(index)

                save_cases(cases)

                st.success(
                    "Case deleted"
                )

                st.rerun()



        st.divider()
