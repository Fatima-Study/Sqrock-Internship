# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🔐 Day 16 — HTTP Security Header Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Focus-Web%20Security-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

</p>

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Objective](#-objective)
- [Technologies Used](#️-technologies-used)
- [Security Headers Checked](#-security-headers-checked)
- [Methodology](#️-methodology)
- [Installation](#-installation)
- [Execution](#️-execution)
- [Testing & Results](#-testing--results)
- [CSP Analysis](#️-csp-analysis)
- [Recommendations](#-recommendations)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)

## 📌 Overview

This project implements a Python-based **HTTP Security Header Analyzer** for identifying missing security configurations in a controlled local web environment.

The analyzer checks important HTTP security headers and reports whether they are configured or missing.

**Target Environment:** `http://localhost:8000`

> ⚠️ **Safety Notice:** This project is intended for authorized and isolated local lab environments only.

## 🎯 Objective

The main objectives of this task are:

- Analyze HTTP response headers.
- Identify missing security headers.
- Understand the security purpose of common HTTP headers.
- Analyze the role of Content Security Policy (CSP).
- Generate an automated security analysis output.

## 🛠️ Technologies Used

- **Python 3.x**
- **Requests**
- **HTTP**
- **Local HTTP Server**
- **Command Prompt**

## 🔍 Security Headers Checked

| Security Header | Security Purpose |
|---|---|
| `Strict-Transport-Security` | Helps enforce HTTPS communication |
| `Content-Security-Policy` | Restricts untrusted scripts and resources |
| `X-Frame-Options` | Helps reduce clickjacking risks |
| `X-Content-Type-Options` | Helps prevent MIME-type sniffing |

## ⚙️ Methodology

```text
Start Local HTTP Server
        ↓
Access localhost:8000
        ↓
Send HTTP GET Request
        ↓
Receive HTTP Response
        ↓
Check Security Headers
        ↓
Identify Missing Headers
        ↓
Display Security Findings
        ↓
Save Output Log
```
---

## 💻 Installation

Check the Python installation:

```bash
py --version
```

Install the required `requests` library:

```bash
py -m pip install requests
```

## ▶️ Execution

Start the local HTTP server:

```bash
py -m http.server 8000
```

Open another Command Prompt window and run:

```bash
py header_analyzer.py
```

To save the execution output:

```bash
py header_analyzer.py > output.txt
```

## 📊 Testing & Results

The local server successfully returned:

```text
HTTP Status Code: 200
```

The analyzer detected the following missing security headers:

```text
[-] VULNERABLE: Missing Security Header -> Strict-Transport-Security
[-] VULNERABLE: Missing Security Header -> Content-Security-Policy
[-] VULNERABLE: Missing Security Header -> X-Frame-Options
[-] VULNERABLE: Missing Security Header -> X-Content-Type-Options
```

### Result Summary

| Test                      | Result     |
| ------------------------- | ---------- |
| Local Server Connectivity | ✅ PASS     |
| HTTP Response             | ✅ 200 OK   |
| HSTS                      | ⚠️ Missing |
| CSP                       | ⚠️ Missing |
| X-Frame-Options           | ⚠️ Missing |
| X-Content-Type-Options    | ⚠️ Missing |

## 🛡️ CSP Analysis

**Content-Security-Policy (CSP)** is an HTTP security mechanism that helps control which scripts and other resources a browser is allowed to load.

A properly configured CSP can reduce the risk of malicious script execution and restrict untrusted resource loading.

## 🔧 Recommendations

* Configure an appropriate **Content-Security-Policy**.
* Enable **HSTS** when HTTPS is properly configured.
* Configure **X-Frame-Options** to reduce clickjacking exposure.
* Configure **X-Content-Type-Options** with `nosniff`.
* Perform regular HTTP security header assessments.

## 📁 Project Structure

```text
Day-16-header-analyzer/
│
├── header_analyzer.py
├── server-running.png
├── output.png
|
└── README.md
```

## 📸 Evidence

The project includes evidence of:

* Local HTTP server execution
* HTTP security header analysis
* Successful HTTP 200 response
* Missing security header detection
* Saved execution output

## ✅ Conclusion

The HTTP Security Header Analysis task was successfully completed in an authorized local environment.

The Python analyzer successfully connected to the local HTTP server, received an HTTP 200 response, and checked four important HTTP security headers. The task demonstrated how Python automation can support defensive web application security assessments.

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  Cybersecurity | SQROCK IT SOLUTION-Internship (Aug-Sep 2026 Batch)
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">GitHub Profile</a> •
  <a href="https://www.linkedin.com/in/fatima-taufique-1313b633b/">LinkedIn</a>
</p>
