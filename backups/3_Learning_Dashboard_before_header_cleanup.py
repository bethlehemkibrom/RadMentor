
import streamlit as st

from utils.storage import load_cases
from utils.theme import apply_theme
from utils.preferences import get_accent_color
from utils.components import page_header, empty_state


apply_theme(get_accent_color())


page_header(
    "📊",
    "Learning Dashboard",
    "Track your radiology learning journey."
)


cases = load_cases()


if not cases:

    empty_state(
        "Add cases to generate your dashboard."
    )


else:


    total = len(cases)


    reviewed = len(
        [
            c for c in cases
            if c.get(
                "review_status"
            ) == "Reviewed"
        ]
    )


    pending = total - reviewed


    important = len(
        [
            c for c in cases
            if c.get(
                "priority"
            ) in [
                "Important",
                "Must review"
            ]
        ]
    )


    with_images = len(
        [
            c for c in cases
            if c.get("image_path")
        ]
    )


    with_resources = len(
        [
            c for c in cases
            if c.get("reference_link")
        ]
    )



    col1, col2, col3 = st.columns(3)


    col1.metric(
        "🩻 Total Cases",
        total
    )


    col2.metric(
        "✅ Reviewed",
        reviewed
    )


    col3.metric(
        "🔁 To Review",
        pending
    )


    col4, col5, col6 = st.columns(3)


    col4.metric(
        "⭐ Important",
        important
    )


    col5.metric(
        "🖼️ Images",
        with_images
    )


    col6.metric(
        "🔗 Resources",
        with_resources
    )



    st.divider()


    st.subheader(
        "📚 Learning Summary"
    )


    st.write(
        """
        Keep building your personal radiology knowledge library.

        Every case reviewed is a step toward stronger pattern
        recognition and clinical confidence.
        """
    )
