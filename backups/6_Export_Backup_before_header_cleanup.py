
import streamlit as st
import json
import csv
import io

from utils.storage import load_cases
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state


apply_theme(get_accent_color())


page_header(
    "📦",
    "Export & Backup",
    "Download and protect your personal radiology learning library."
)


cases = load_cases()


if not cases:

    empty_state(
        "No cases available for export."
    )


else:


    st.success(
        f"{len(cases)} cases ready for backup."
    )



    st.subheader(
        "📄 JSON Backup"
    )


    json_data = json.dumps(
        cases,
        indent=4
    )


    st.download_button(
        label="⬇️ Download JSON Backup",
        data=json_data,
        file_name="RadMentor_cases_backup.json",
        mime="application/json"
    )



    st.divider()



    st.subheader(
        "📊 CSV Teaching File"
    )


    output = io.StringIO()


    writer = csv.writer(output)


    writer.writerow(
        [
            "Diagnosis",
            "Modality",
            "Body System",
            "Difficulty",
            "Clinical History",
            "Findings",
            "Teaching Pearls",
            "Learning Points",
            "Reference"
        ]
    )


    for case in cases:

        writer.writerow(
            [
                case.get("diagnosis",""),
                case.get("modality",""),
                case.get("body_system",""),
                case.get("difficulty",""),
                case.get("clinical_history",""),
                case.get("findings",""),
                case.get("notes",""),
                case.get("learning_points",""),
                case.get("reference_link","")
            ]
        )



    st.download_button(
        label="⬇️ Download CSV Teaching File",
        data=output.getvalue(),
        file_name="RadMentor_teaching_file.csv",
        mime="text/csv"
    )
