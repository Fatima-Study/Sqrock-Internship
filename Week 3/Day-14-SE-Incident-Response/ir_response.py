import datetime
import json


def ir_response(incident):

    print("\n" + "=" * 60)
    print("        INCIDENT RESPONSE TRIGGERED")
    print("=" * 60)

    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"User     : {incident['user']}")

    actions = []

    # High/Critical severity actions
    if incident["severity"] in ("HIGH", "CRITICAL"):

        actions += [
            "SIMULATION: Lock user account",
            "SIMULATION: Revoke active sessions",
            "Notify SOC team",
            "Preserve mail logs"
        ]

    # Phishing-specific actions
    if incident["type"] == "phishing":

        actions += [
            "Quarantine suspicious email",
            "Block sender domain",
            "Scan attachment in sandbox"
        ]

    print("\nActions Taken:")

    for action in actions:
        print(f" [x] {action}")

    # Create report
    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    with open("ir_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nIR report saved: ir_report.json")
    print("\nIncident response simulation completed successfully!")


if __name__ == "__main__":

    incident = {
        "type": "phishing",
        "severity": "HIGH",
        "user": "lab_user@example.com"
    }

    ir_response(incident)
