def fake_profile_score(profile):
    score = 0

    # New account
    age_days = profile.get("account_age_days", 365)

    if age_days < 30:
        score += 30

    # Follower/following ratio
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)

    ratio = following / max(followers, 1)

    if ratio > 10:
        score += 25

    # Profile picture
    if profile.get("no_profile_pic"):
        score += 20

    # Number of posts
    if profile.get("posts", 100) < 5:
        score += 15

    # Default bio
    if profile.get("default_bio"):
        score += 10

    return min(score, 100)


profiles = [
    {
        "name": "Profile A",
        "account_age_days": 7,
        "followers": 2,
        "following": 900,
        "no_profile_pic": True,
        "posts": 1,
        "default_bio": True
    },

    {
        "name": "Profile B",
        "account_age_days": 1200,
        "followers": 4500,
        "following": 320,
        "no_profile_pic": False,
        "posts": 870,
        "default_bio": False
    }
]


for profile in profiles:
    score = fake_profile_score(profile)

    if score >= 60:
        risk = "HIGH RISK"
    elif score >= 30:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    print(
        f"{profile['name']} -> "
        f"Fake Score: {score}% -> {risk}"
    )
