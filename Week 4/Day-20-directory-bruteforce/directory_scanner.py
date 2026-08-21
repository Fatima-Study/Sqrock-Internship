import requests


def audit_directory_paths(base_url, wordlist):
    print(f"[*] Discovering endpoints for: {base_url}")
    print("-" * 60)

    for directory in wordlist:
        target_path = f"{base_url}/{directory}"

        try:
            response = requests.get(target_path, timeout=3)

            if response.status_code == 200:
                print(
                    f"[MATCH DETECTED] Route accessible: "
                    f"{target_path} (Status: 200)"
                )

            elif response.status_code == 403:
                print(
                    f"[RESTRICTED ROUTE] Forbidden resource mapped: "
                    f"{target_path} (Status: 403)"
                )

            else:
                print(
                    f"[-] Not Accessible: "
                    f"{target_path} (Status: {response.status_code})"
                )

        except requests.RequestException:
            print(f"[!] Request failed: {target_path}")


audit_directory_paths(
    "http://localhost:5000",
    ["admin", "dashboard", "api/v1", ".env", "backup.sql"]
)