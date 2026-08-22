# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🔐 Day 21 — Cross-Site Scripting (XSS) Payload Sanitizer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Security](https://img.shields.io/badge/Focus-XSS%20Protection-red)
![Input Sanitization](https://img.shields.io/badge/Technique-Input%20Sanitization-orange)
![Defensive Coding](https://img.shields.io/badge/Approach-Defensive%20Coding-purple)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-blueviolet)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Objective](#-objective)
- [Technologies Used](#️-technologies-used)
- [XSS Security Checks](#-xss-security-checks)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [XSS Analysis](#-xss-analysis)
- [Security Recommendations](#-security-recommendations)
- [Result Summary](#-result-summary)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **Cross-Site Scripting (XSS) Payload Sanitizer** for identifying and neutralizing common client-side injection patterns.

The sanitizer uses HTML encoding and pattern filtering to process untrusted user input and neutralize selected XSS-related tokens, including:

- `script`
- `onerror`
- `onload`

The implementation was tested against **10 explicit adversarial test parameters** in a controlled local environment.

> ⚠️ **Safety Notice:** This project is intended for authorized local or isolated lab environments only.

---

## 🎯 Objective

The main objectives of this task are:

- Implement a Python-based XSS payload sanitizer.
- Encode HTML special characters using `html.escape()`.
- Identify and neutralize selected XSS-related patterns.
- Test the sanitizer against 10 adversarial inputs.
- Verify the sanitized output.
- Understand Stored, Reflected, and DOM-based XSS models.
- Develop basic defensive input-handling skills.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **HTML Encoding**
- **Python `html` Module**
- **Python `re` Module**
- **Regular Expressions**
- **Command Prompt**
- **Local Security Lab**

---

## 🔍 XSS Security Checks

The sanitizer performs the following checks:

| Security Check | Description | Result |
|---|---|---|
| HTML Encoding | Converts HTML special characters into encoded entities | ✅ Applied |
| `script` Detection | Identifies script-related input | ✅ Neutralized |
| `onerror` Detection | Identifies event-handler based input | ✅ Neutralized |
| `onload` Detection | Identifies event-handler based input | ✅ Neutralized |
| Adversarial Testing | Tests sanitizer against 10 inputs | ✅ Completed |

---

## ⚙️ Methodology

```text
User Input
    ↓
Python Sanitizer
    ↓
HTML Encoding
    ↓
Pattern Detection
    ↓
Prohibited Token Replacement
    ↓
Sanitized Output
    ↓
10 Adversarial Tests
    ↓
Result Verification
    ↓
XSS Security Analysis
```
---

## 💻 Implementation

The sanitizer uses Python's built-in `html` module and regular expressions.

### 1. HTML Encoding

The input is first processed using:

```python
encoded_string = html.escape(raw_payload)
```

This converts HTML special characters into encoded representations.

For example:

```text
<script>alert('XSS')</script>
```

is converted into an encoded form where the HTML characters are no longer interpreted as normal markup.

### 2. Prohibited Token Filtering

The implementation then checks selected patterns:

```python
stripped_output = re.sub(
    r"(?i)script|onerror|onload",
    "[PROHIBITED_TOKEN]",
    encoded_string
)
```

Detected tokens are replaced with:

```text
[PROHIBITED_TOKEN]
```

### 3. Sanitization Function

```python
def sanitize_user_input(raw_payload):
    encoded_string = html.escape(raw_payload)

    stripped_output = re.sub(
        r"(?i)script|onerror|onload",
        "[PROHIBITED_TOKEN]",
        encoded_string
    )

    return stripped_output
```

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-21-XSS-Payload-Sanitizer
```

Run the sanitizer:

```cmd
python xss_sanitizer.py
```

To save the execution output:

```cmd
python xss_sanitizer.py > xss_test_output.txt
```

To view the saved output:

```cmd
type xss_test_output.txt
```

---

## 📊 Testing and Results

The sanitizer was tested against **10 adversarial parameters** containing different XSS-related patterns.

### Test Cases

| Test | Input Pattern                             | Result        |
| ---- | ----------------------------------------- | ------------- |
| 1    | `<script>alert('XSS')</script>`           | ✅ Neutralized |
| 2    | `<img src=x onerror=alert('XSS')>`        | ✅ Neutralized |
| 3    | `<body onload=alert('XSS')>`              | ✅ Neutralized |
| 4    | `<script>document.cookie</script>`        | ✅ Neutralized |
| 5    | `<svg onload=alert('XSS')>`               | ✅ Neutralized |
| 6    | JavaScript URI pattern                    | ✅ Sanitized   |
| 7    | HTML event-handler pattern                | ✅ Neutralized |
| 8    | `<script>alert(document.domain)</script>` | ✅ Neutralized |
| 9    | Image `onerror` pattern                   | ✅ Neutralized |
| 10   | `<script>console.log('test')</script>`    | ✅ Neutralized |

---

## 🔬 XSS Analysis

### 1. Stored XSS

Stored XSS occurs when malicious input is stored by an application and later delivered to users through a web page.

```text
Attacker Input
      ↓
Web Application
      ↓
Stored Data
      ↓
Victim Browser
```

### 2. Reflected XSS

Reflected XSS occurs when untrusted input is included in a request and is reflected back in the application's response.

```text
User Request
      ↓
Web Application
      ↓
HTTP Response
      ↓
Browser
```

### 3. DOM-Based XSS

DOM-based XSS occurs when client-side JavaScript processes untrusted input and places it into the browser DOM in an unsafe manner.

```text
User Input
      ↓
Client-Side JavaScript
      ↓
DOM Manipulation
      ↓
Browser
```

---

## 🛡️ Security Recommendations

### Validate User Input

Applications should validate and handle untrusted input before processing it.

### Apply HTML Encoding

HTML output should be encoded according to the context in which the data is displayed.

### Avoid Unsafe DOM Operations

Client-side applications should avoid placing untrusted data directly into HTML or other executable contexts.

### Use Content Security Policy

A properly configured **Content Security Policy (CSP)** can provide an additional layer of protection against script injection.

### Perform Security Testing

Input-handling mechanisms should be regularly tested against different malicious and adversarial patterns.

---

## 📋 Result Summary

```text
Sanitizer Implementation      → PASS
HTML Encoding                 → PASS
Pattern Filtering             → PASS
10 Adversarial Tests          → PASS
Output Verification           → PASS
XSS Analysis                  → PASS
```

### Overall Findings

| Security Check      | Result         |
| ------------------- | -------------- |
| HTML Encoding       | ✅ Applied      |
| `script` Pattern    | 🔴 Neutralized |
| `onerror` Pattern   | 🔴 Neutralized |
| `onload` Pattern    | 🔴 Neutralized |
| 10 Test Parameters  | ✅ Completed    |
| Sanitizer Execution | ✅ Successful   |

---

## 📁 Project Structure

```text
Day-21-XSS-Payload-Sanitizer/
│
├── xss_sanitizer.py
├── output.png
│
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* XSS sanitizer implementation.
* HTML encoding process.
* Prohibited token filtering.
* Ten adversarial test cases.
* Sanitized output generation.
* Successful Python execution.
* XSS validation results.

---

## ✅ Conclusion

The **Cross-Site Scripting (XSS) Payload Sanitizer** was successfully implemented and tested in a controlled local environment.

The sanitizer successfully processed ten adversarial test parameters using HTML encoding and selected pattern filtering techniques.

This task provided practical experience in defensive input sanitization and improved understanding of **Stored, Reflected, and DOM-based XSS** security models.

---

<a name="author-contact"></a>

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  Cybersecurity | SQROCK IT SOLUTION - Internship (Aug-Sep 2026 Batch)
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">
    GitHub
  </a>
  |
  <a href="https://linkedin.com/in/fatima-taufique-1313b633b">
    LinkedIn
  </a>
</p>
