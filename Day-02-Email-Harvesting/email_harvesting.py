import requests
import re


def find_emails(url):
    print("=" * 40)
    print("      EMAIL HARVESTING TOOL")
    print("=" * 40)

    print(f"\nURL: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html = response.text

        # Find email addresses using regex
        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        emails = re.findall(email_pattern, html)

        # Remove duplicates
        emails = sorted(set(emails))

        print("\nEmails Found:")

        if emails:
            for number, email in enumerate(emails, start=1):
                print(f"{number}. {email}")

            print(f"\nTotal Emails Found: {len(emails)}")
        else:
            print("No email addresses found.")
            print("\nTotal Emails Found: 0")

    except requests.RequestException as error:
        print(f"\nError accessing webpage: {error}")

    print("\nEmail harvesting completed successfully.")


# Authorized practice webpage
url = "http://localhost:8000/lab_page.html"

find_emails(url)
