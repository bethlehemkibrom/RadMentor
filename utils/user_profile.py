
import json
from pathlib import Path


PROFILE_FILE = Path("user_profile.json")


def save_profile(name, email):

    profile = {
        "name": name,
        "email": email
    }

    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)



def load_profile():

    if PROFILE_FILE.exists():

        with open(PROFILE_FILE, "r") as f:
            return json.load(f)

    return {
        "name": "",
        "email": ""
    }
