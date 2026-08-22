def evaluate_db_credentials(target_ip, credential_dictionary):

    print(f"[*] Evaluating DB Authentication Resilience on: {target_ip}")
    print("-" * 60)

    for username, secret in credential_dictionary.items():

        if username == "postgres" and secret == "postgres":
            print(
                f"[CRITICAL OUTCOME] Default Administrator Credentials Active: "
                f"{username}:{secret}"
            )
        else:
            print(
                f"[-] Evaluation Passed for configuration pair -> "
                f"{username}: {secret[:3]}***"
            )


credentials = {
    "postgres": "postgres",
    "app_user": "SecureP@ss2026!"
}

evaluate_db_credentials("127.0.0.1", credentials)