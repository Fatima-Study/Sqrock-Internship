def spear_phish_template(target):
    return f"""
===============================
PHISHING AWARENESS EMAIL
LAB SIMULATION ONLY
===============================

From: it-support@{target['company'].lower()}.com
To: {target['email']}

Subject: Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.

Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team

--- Awareness Red Flags ---
1. Urgent language
2. Account suspension threat
3. Unexpected login notification
4. Request to click a verification link

This email is for authorized security-awareness training only.
"""


targets = [
    {
        "name": "Riya Sharma",
        "email": "riya@example.com",
        "company": "Sqrock",
        "location": "Bangalore, India"
    },
    {
        "name": "Ali Khan",
        "email": "ali@example.com",
        "company": "CyberLab",
        "location": "Karachi, Pakistan"
    },
    {
        "name": "Sara Ahmed",
        "email": "sara@example.com",
        "company": "SecureLab",
        "location": "Lahore, Pakistan"
    }
]


for target in targets:
    print(spear_phish_template(target))
