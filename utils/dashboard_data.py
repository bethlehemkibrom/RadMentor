
def get_dashboard_stats(cases):

    total_cases = len(cases)

    modalities = len(
        set(
            c.get("modality")
            for c in cases
            if c.get("modality")
        )
    )

    body_systems = len(
        set(
            c.get("body_system")
            for c in cases
            if c.get("body_system")
        )
    )

    pending = len(
        [
            c for c in cases
            if c.get("review_status") != "Reviewed"
        ]
    )

    return {
        "total_cases": total_cases,
        "modalities": modalities,
        "body_systems": body_systems,
        "pending": pending
    }
