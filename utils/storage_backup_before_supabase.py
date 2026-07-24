
"""
RadMentor Storage Manager

This module is the only place responsible for
loading and saving cases.

Later it will automatically decide whether
to use:

- Local JSON
- Supabase Cloud
"""

import json
from pathlib import Path


CASE_FILE = Path("data/cases.json")


def load_cases():
    """
    Load all cases.

    Currently:
        Local JSON

    Future:
        Supabase
    """

    if not CASE_FILE.exists():
        return []

    with open(CASE_FILE, "r") as f:
        return json.load(f)


def save_cases(cases):
    """
    Save all cases.

    Currently:
        Local JSON

    Future:
        Supabase
    """

    CASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(CASE_FILE, "w") as f:
        json.dump(
            cases,
            f,
            indent=4
        )


def get_total_cases():

    return len(load_cases())


def clear_cases():

    save_cases([])
