
import streamlit as st
from datetime import datetime
from utils.storage import load_cases, save_cases
import uuid

from utils.supabase_client import supabase
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header


apply_theme(get_accent_color())


page_header(
    "➕",
    "Add Case",
    "Save your radiology learning case to your cloud library."
)


if "user" not in st.session_state or st.session_state.user is None:

    st.warning(
        "Please login first from the Account page."
    )

    st.stop()



user = st.session_state.user



diagnosis = st.text_input(
    "Final Diagnosis"
)


modality = st.selectbox(
    "Modality",
    [
        "X-ray",
        "Ultrasound",
        "CT",
        "MRI",
        "Fluoroscopy",
        "Interventional Radiology"
    ]
)


body_system = st.selectbox(
    "Body System",
    [
        "Brain",
        "Chest",
        "Abdomen",
        "Musculoskeletal",
        "Cardiovascular",
        "Pediatrics",
        "Other"
    ]
)


clinical_history = st.text_area(
    "Clinical History"
)


findings = st.text_area(
    "Imaging Findings"
)


differential = st.text_area(
    "Differential Diagnosis"
)


teaching_pearls = st.text_area(
    "Teaching Pearls"
)


learning_points = st.text_area(
    "Key Learning Points"
)


reference_title = st.text_input(
    "Reference Title"
)


reference_link = st.text_input(
    "Journal / Website Link"
)


source = st.text_input(
    "Source"
)



if st.button("💾 Save Case"):


    case = {

        "id": str(uuid.uuid4()),

        "user_id": user.id,

        "diagnosis": diagnosis,

        "modality": modality,

        "body_system": body_system,

        "clinical_history": clinical_history,

        "findings": findings,

        "differential": differential,

        "teaching_pearls": teaching_pearls,

        "learning_points": learning_points,

        "reference_title": reference_title,

        "reference_link": reference_link,

        "source": source,

        "review_status": "Not reviewed",

        "priority": "Normal",

        "created_at": str(datetime.now())

    }



    response = supabase.table(
        "cases"
    ).insert(
        case
    ).execute()



    st.success(
        "Case saved to cloud successfully 🩻"
    )
