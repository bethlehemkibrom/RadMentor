import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="RadMentor",
    page_icon="🩻"
)

CASE_FILE = "data/cases.json"


def load_cases():
    if os.path.exists(CASE_FILE):
        with open(CASE_FILE, "r") as file:
            return json.load(file)
    return []


def save_cases(cases):
    with open(CASE_FILE, "w") as file:
        json.dump(cases, file, indent=4)


st.title("🩻 RadMentor")

st.subheader(
    "Your intelligent companion through radiology training"
)

st.write(
    "Capture cases, review knowledge, and grow as a radiologist."
)

st.divider()

st.header("➕ Add a Case")

diagnosis = st.text_input("Diagnosis")

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

notes = st.text_area("Teaching pearls")


if st.button("Save Case"):

    cases = load_cases()

    new_case = {
        "diagnosis": diagnosis,
        "modality": modality,
        "notes": notes,
        "date": str(datetime.now().date())
    }

    cases.append(new_case)

    save_cases(cases)

    st.success("Case saved successfully! 🩻")


st.divider()

st.header("📚 My Cases")

cases = load_cases()

if len(cases) == 0:
    st.info("No cases saved yet.")

else:
    for index, case in enumerate(cases):

        st.subheader(
            f"{index + 1}. {case['diagnosis']}"
        )

        st.write(
            f"**Modality:** {case['modality']}"
        )

        st.write(
            f"**Teaching pearls:** {case['notes']}"
        )

        st.write(
            f"**Saved:** {case['date']}"
        )
