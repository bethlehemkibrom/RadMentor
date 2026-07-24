
import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")


def save_accent_color(color):

    settings = {
        "accent_color": color
    }

    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)



def get_accent_color():

    if SETTINGS_FILE.exists():

        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)

        return settings.get(
            "accent_color",
            "#C98295"
        )

    return "#C98295"
