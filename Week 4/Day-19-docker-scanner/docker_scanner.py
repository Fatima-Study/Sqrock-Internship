def analyze_dockerfile(path):
    print(f"[*] Parsing Container Directives: {path}")
    print("-" * 60)

    has_explicit_user = False

    try:
        with open(path, "r") as file:

            for idx, line in enumerate(file, 1):

                cleaned = line.strip().upper()

                # Check USER directive
                if cleaned.startswith("USER"):
                    has_explicit_user = True

                # Check latest tag
                if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                    print(
                        f"[RISK DETECTED] Line {idx}: "
                        "Base image uses unpinned 'latest' tag."
                    )

                # Check SSH exposure
                if "EXPOSE 22" in cleaned:
                    print(
                        f"[CRITICAL PROHIBITED] Line {idx}: "
                        "SSH protocol channel exposed on Port 22."
                    )

        # Check if USER directive is missing
        if not has_explicit_user:
            print(
                "[RISK DETECTED] No explicit USER directive found. "
                "Container may run with default privileges."
            )
        else:
            print("[+] Explicit USER directive detected.")

    except FileNotFoundError:
        print(f"[!] Error: Dockerfile not found - {path}")


analyze_dockerfile("Dockerfile")