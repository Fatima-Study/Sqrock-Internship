import whois
import socket
import requests


def osint_scan(domain):
    print("=" * 40)
    print("        OSINT SCANNER")
    print("=" * 40)

    print(f"\nDomain: {domain}")

    # WHOIS information
    try:
        w = whois.whois(domain)
        print(f"Registrar: {w.registrar}")
    except Exception as e:
        print(f"Registrar: Unable to retrieve")

    # IP address
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
    except Exception as e:
        print("IP Address: Unable to retrieve")
        return

    # IP geolocation
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=10
        )

        geo = response.json()

        print(f"City: {geo.get('city')}")
        print(f"Country: {geo.get('country')}")
    except Exception as e:
        print("Location: Unable to retrieve")

    print("\nOSINT Scan Completed Successfully.")


domain = "example.com"
osint_scan(domain)
