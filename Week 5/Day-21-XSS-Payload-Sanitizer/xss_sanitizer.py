import html
import re

def sanitize_user_input(raw_payload):
    encoded_string = html.escape(raw_payload)

    stripped_output = re.sub(
        r"(?i)script|onerror|onload",
        "[PROHIBITED_TOKEN]",
        encoded_string
    )

    return stripped_output


test_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<script>document.cookie</script>",
    "<svg onload=alert('XSS')>",
    "<iframe src='javascript:alert(1)'>",
    "<div onerror='alert(1)'>",
    "<script>alert(document.domain)</script>",
    "<img src='x' onerror='alert(1)'>",
    "<script>console.log('test')</script>"
]

print("=== XSS PAYLOAD SANITIZER ===\n")

for number, payload in enumerate(test_payloads, 1):
    sanitized = sanitize_user_input(payload)

    print(f"Test {number}")
    print(f"Raw Input: {payload}")
    print(f"Sanitized: {sanitized}")
    print("-" * 60)