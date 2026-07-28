
import streamlit as st

from utils.storage import load_cases, save_cases
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state


apply_theme(get_accent_color())


page_header(
    "📝",
    "Edit Case",
    "Update and improve your radiology learning cases."
)


cases = load_cases()


if not cases:

    empty_state(
        "No cases available to edit."
    )


else:


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


    reference_title = st.text_input(
        "Reference Title",
        case.get("reference_title","")
    )


    reference_link = st.text_input(
        "Reference Link",
        case.get("reference_link","")
    )



    if st.button("💾 Save Changes"):


        cases[index]["diagnosis"] = diagnosis

        cases[index]["clinical_history"] = clinical_history

        cases[index]["findings"] = findings

        cases[index]["differential"] = differential

        cases[index]["notes"] = notes

        cases[index]["learning_points"] = learning_points

        cases[index]["reference_title"] = reference_title

        cases[index]["reference_link"] = reference_link


        save_cases(cases)


        st.success(
            "Case updated successfully ✅"
        )
