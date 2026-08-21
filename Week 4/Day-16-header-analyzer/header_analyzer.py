import requests


def verify_headers(url):
    print(f"[*] Auditing Target Headers: {url}")

    target_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    try:
        response = requests.get(url, timeout=5)

        print(f"[*] HTTP Status Code: {response.status_code}")
        print()

        for header in target_headers:
            if header in response.headers:
                print(f"[+] CONFIGURED: {header}")
                print(f"    Value: {response.headers[header]}")
            else:
                print(f"[-] VULNERABLE: Missing Security Header -> {header}")

    except requests.RequestException as e:
        print(f"[!] Target Unreachable: {e}")


verify_headers("http://localhost:8000")