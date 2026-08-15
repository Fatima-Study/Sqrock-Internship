import re
from collections import Counter

LOG_SAMPLE = """
2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:16 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:18 SUCCESS_LOGIN user=admin ip=45.33.32.156
2024-01-15 08:00:01 SUCCESS_LOGIN user=riya ip=192.168.1.10
2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
"""

def analyze_logs(logs):

    print("=" * 60)
    print("        SIEM LOG ANALYSIS")
    print("=" * 60)

    # Find failed login attempts
    fails = re.findall(
        r'FAILED_LOGIN user=(\w+) ip=([\d.]+)',
        logs
    )

    # Find suspicious email rules
    rules = re.findall(
        r'EMAIL_RULE_CREATED user=(\w+)',
        logs
    )

    # Count failed login attempts per user
    fail_counts = Counter(user for user, ip in fails)

    print("\nAnalyzing security logs...\n")

    alerts = []

    # Detect repeated failed logins
    for user, count in fail_counts.items():

        if count >= 3:
            alert = (
                f"[ALERT] Brute force detected: "
                f"{user} ({count} failed attempts)"
            )

            print(alert)
            alerts.append(alert)

    # Detect suspicious email rules
    for user in rules:

        alert = (
            f"[ALERT] Suspicious email rule created by: {user}"
        )

        print(alert)
        alerts.append(alert)

    # Final report
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)

    print(f"Failed login events: {len(fails)}")
    print(f"Suspicious email rules: {len(rules)}")
    print(f"Alerts generated: {len(alerts)}")

    print("\nLog analysis completed successfully!")


if __name__ == "__main__":
    analyze_logs(LOG_SAMPLE)
