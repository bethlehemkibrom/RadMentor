
import streamlit as st

from components.hero import hero
from components.metric_cards import metric_cards
from components.today_focus import today_focus
from components.clinical_pearl import clinical_pearl
from components.activity_feed import activity_feed
from components.quick_actions import quick_actions
from components.growth_chart import growth_chart

from utils.dashboard_data import get_dashboard_stats
from utils.analytics import calculate_learning_stats


def dashboard(user=None, cases=None):

    if cases is None:
        cases = []


    stats = get_dashboard_stats(cases)

    learning_stats = calculate_learning_stats(cases)


    hero(user)


    st.markdown(
        "## Knowledge Overview"
    )


    metric_cards(
        total_cases=stats["total_cases"],
        modalities=stats["modalities"],
        body_systems=stats["body_systems"],
        pending=stats["pending"]
    )


    today_focus()


    clinical_pearl()


    recent = []

    for case in cases[:5]:

        diagnosis = case.get(
            "diagnosis",
            "Unnamed case"
        )

        recent.append(
            f"Reviewed case: {diagnosis}"
        )


    activity_feed(
        recent
    )


    growth_chart()

    quick_actions()
