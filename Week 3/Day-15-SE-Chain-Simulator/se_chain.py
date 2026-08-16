import sys


MODULES = {
    "osint": "Run passive OSINT on a practice domain",
    "profile": "Build a sample target profile",
    "phish": "Score a URL for phishing indicators",
    "template": "Generate a phishing-awareness email",
    "ir": "Trigger incident response workflow"
}


def menu():
    print("\n" + "=" * 60)
    print("          SE CHAIN SIMULATOR")
    print("       SQROCK CYBERSECURITY INTERNSHIP")
    print("=" * 60)

    for key, description in MODULES.items():
        print(f" [{key}] {description}")

    print(" [exit] Exit simulator")

    choice = input("\nSelect module: ").strip().lower()

    if choice == "exit":
        print("\nSimulator closed.")
        sys.exit()

    if choice in MODULES:
        print(f"\n[+] Launching {choice} module...")

        if choice == "osint":
            run_osint()

        elif choice == "profile":
            run_profile()

        elif choice == "phish":
            run_phish()

        elif choice == "template":
            run_template()

        elif choice == "ir":
            run_ir()

    else:
        print("\n[-] Invalid choice.")

    menu()


def run_osint():
    print("\n--- OSINT MODULE ---")
    print("Practice Domain: example.com")
    print("Purpose: Passive information gathering")
    print("Status: Simulation completed.")


def run_profile():
    print("\n--- PROFILE MODULE ---")

    profile = {
        "name": "Lab User",
        "role": "Cybersecurity Trainee",
        "tech_stack": ["Python", "GitHub"],
        "environment": "Authorized Lab"
    }

    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\nProfile generation completed.")


def run_phish():
    print("\n--- PHISHING SCORE MODULE ---")

    url = "https://example.com"

    score = 0

    if not url.startswith("https"):
        score += 30

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "account",
        "bank"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 20

    score = min(score, 100)

    print(f"URL: {url}")
    print(f"Phishing Risk Score: {score}%")
    print("Purpose: Awareness training only.")


def run_template():
    print("\n--- EMAIL TEMPLATE MODULE ---")

    email = """
=== PHISHING AWARENESS TRAINING EMAIL ===

From: security-training@example.com
To: lab-user@example.com
Subject: Security Verification Awareness Exercise

Hello Lab User,

This is a simulated cybersecurity awareness exercise.
Please review this message and identify suspicious indicators.

RED FLAGS:
- Urgency
- Unexpected verification request
- Suspicious links
- Request for sensitive information

Training purpose only.
"""

    print(email)


def run_ir():
    print("\n--- INCIDENT RESPONSE MODULE ---")

    incident = {
        "type": "phishing",
        "severity": "HIGH"
    }

    print(f"Incident Type : {incident['type']}")
    print(f"Severity      : {incident['severity']}")

    print("\nResponse Actions:")

    actions = [
        "SIMULATION: Lock affected account",
        "SIMULATION: Revoke active sessions",
        "Notify SOC team",
        "Preserve security logs",
        "Quarantine suspicious email"
    ]

    for action in actions:
        print(f"[x] {action}")

    print("\nIncident response simulation completed.")


if __name__ == "__main__":
    menu()
5
