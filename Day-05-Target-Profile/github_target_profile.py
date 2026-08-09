import requests
import json


def github_profile(username):
    base_url = "https://api.github.com"

    user_response = requests.get(f"{base_url}/users/{username}")
    repos_response = requests.get(f"{base_url}/users/{username}/repos")

    if user_response.status_code != 200:
        print("Unable to retrieve GitHub profile.")
        return

    user = user_response.json()
    repos = repos_response.json()

    languages = {}

    for repo in repos[:10]:
        language = repo.get("language")

        if language:
            languages[language] = languages.get(language, 0) + 1

    profile = {
        "name": user.get("name"),
        "company": user.get("company"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "top_langs": languages,
        "bio": user.get("bio")
    }

    print("=" * 50)
    print("       GITHUB TARGET PROFILE")
    print("=" * 50)
    print(json.dumps(profile, indent=4))

    with open("target_profile.json", "w") as file:
        json.dump(profile, file, indent=4)

    print("\nProfile JSON saved successfully.")


github_profile("torvalds")
