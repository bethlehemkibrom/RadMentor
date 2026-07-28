
from datetime import datetime


def calculate_learning_stats(cases):

    total_cases = len(cases)

    reviewed = len(
        [
            c for c in cases
            if c.get("review_status") == "Reviewed"
        ]
    )

    pending = total_cases - reviewed


    modalities = {}

    for case in cases:

        modality = case.get("modality")

        if modality:
            modalities[modality] = (
                modalities.get(modality, 0) + 1
            )


    body_systems = {}

    for case in cases:

        system = case.get("body_system")

        if system:
            body_systems[system] = (
                body_systems.get(system, 0) + 1
            )


    return {
        "total_cases": total_cases,
        "reviewed": reviewed,
        "pending": pending,
        "modalities": modalities,
        "body_systems": body_systems
    }
