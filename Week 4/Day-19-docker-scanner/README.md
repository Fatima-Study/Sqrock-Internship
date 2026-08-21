# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🐳 Day 19 — Docker Container Misconfiguration Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Docker](https://img.shields.io/badge/Technology-Docker-2496ED?logo=docker)
![Static Analysis](https://img.shields.io/badge/Analysis-Static%20Analysis-orange)
![Container Security](https://img.shields.io/badge/Focus-Container%20Security-red)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

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
- [Security Checks](#-security-checks)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Security Findings](#-security-findings)
- [Security Recommendations](#-security-recommendations)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **Docker Container Misconfiguration Scanner** for performing static security analysis of a Dockerfile.

The scanner reads Dockerfile configuration directives and checks for selected security misconfigurations, including:

- Unpinned `latest` base image tags.
- SSH exposure through port `22`.
- Missing explicit `USER` configuration.

The analysis is performed locally without deploying or attacking any real container.

> ⚠️ **Safety Notice:** This project is intended for authorized local or isolated lab environments only.

---

## 🎯 Objective

The main objectives of this task are:

- Analyze Dockerfile configuration directives.
- Detect the use of an unpinned `latest` image tag.
- Detect SSH exposure through port `22`.
- Check whether an explicit `USER` directive is configured.
- Generate security warnings for detected misconfigurations.
- Understand basic container security hardening practices.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Dockerfile**
- **Python File Handling**
- **String-Based Static Analysis**
- **Command Prompt**
- **Local Security Lab**

---

## 🔍 Security Checks

The scanner performs the following checks:

| Security Check | Description | Severity |
|---|---|---|
| `FROM ...:latest` | Detects an unpinned base image tag | ⚠️ Risk |
| `EXPOSE 22` | Detects SSH exposure on port 22 | 🔴 Critical |
| Missing `USER` | Checks for an explicit user directive | ⚠️ Risk |

---

## ⚙️ Methodology

```text
Dockerfile
    ↓
Python Scanner
    ↓
Read Dockerfile Lines
    ↓
Analyze Configuration Directives
    ↓
Check Security Rules
    ↓
Detect Misconfigurations
    ↓
Generate Security Warnings
    ↓
Save Output
```
---

## 💻 Implementation

The scanner uses Python file handling to read the Dockerfile line by line.

It checks:

### 1. Unpinned Base Image

```dockerfile
FROM ubuntu:latest
```

The scanner identifies the use of the `latest` tag.

### 2. SSH Port Exposure

```dockerfile
EXPOSE 22
```

The scanner identifies exposure of port `22`, which is commonly associated with SSH.

### 3. Explicit USER Directive

The scanner checks whether the Dockerfile contains a `USER` instruction.

If no explicit `USER` directive is found, a security warning is generated.

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-19-docker-scanner
```

Run the scanner:

```cmd
py docker_scanner.py
```

To save the output:

```cmd
py docker_scanner.py > output.txt
```

To view the saved output:

```cmd
type output.txt
```

---

## 📊 Testing and Results

The scanner was successfully executed against the test Dockerfile.

### Actual Output

```text
[*] Parsing Container Directives: Dockerfile
------------------------------------------------------------
[RISK DETECTED] Line 1: Base image uses unpinned 'latest' tag.
[CRITICAL PROHIBITED] Line 5: SSH protocol channel exposed on Port 22.
[RISK DETECTED] No explicit USER directive found. Container may run with default privileges.
```

---

## 🚨 Security Findings

### Finding 1 — Unpinned `latest` Tag

```dockerfile
FROM ubuntu:latest
```

The scanner detected the use of the `latest` tag.

Using a specific and controlled image version can make container builds more predictable and easier to audit.

**Detection:**

```text
[RISK DETECTED]
Base image uses unpinned 'latest' tag.
```

---

### Finding 2 — SSH Port 22 Exposed

```dockerfile
EXPOSE 22
```

The scanner detected SSH exposure on port `22`.

Unnecessary network exposure can increase the attack surface of a container.

**Detection:**

```text
[CRITICAL PROHIBITED]
SSH protocol channel exposed on Port 22.
```

---

### Finding 3 — Missing Explicit USER Directive

The Dockerfile does not contain an explicit `USER` directive.

The scanner therefore reports:

```text
[RISK DETECTED]
No explicit USER directive found.
Container may run with default privileges.
```

Using an appropriate non-root application user can help reduce unnecessary privileges.

---

## 🛡️ Security Recommendations

### Use a Specific Base Image

Instead of:

```dockerfile
FROM ubuntu:latest
```

Use a controlled version such as:

```dockerfile
FROM ubuntu:24.04
```

### Avoid Unnecessary SSH Exposure

If SSH is not required, avoid exposing:

```dockerfile
EXPOSE 22
```

### Configure an Explicit User

Where appropriate, create and use a non-root application user:

```dockerfile
RUN useradd -m appuser

USER appuser
```

These practices can help improve container security and reduce unnecessary attack surface.

---

## 📋 Result Summary

```text
Dockerfile Parsing       → PASS
Latest Tag Detection     → PASS
SSH Port Detection       → PASS
USER Configuration Check → PASS
Security Warning Output  → PASS
```

### Overall Findings

| Check                 | Result       |
| --------------------- | ------------ |
| Unpinned `latest` tag | 🚨 Detected  |
| SSH Port `22`         | 🔴 Critical  |
| Missing `USER`        | 🚨 Detected  |
| Scanner Execution     | ✅ Successful |

---

## 📁 Project Structure

```text
Day-19-docker-scanner/
│
├── Docker-file.txt
├── docker_scanner.py
├── output.png
|
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Dockerfile static analysis.
* Base image tag detection.
* SSH port detection.
* `USER` directive verification.
* Security warning generation.
* Successful scanner execution.
* Saved scan output.

### Screenshot

> **Figure 1: Dockerfile Misconfiguration Scanner Output**

---

## ✅ Conclusion

The **Docker Container Misconfiguration Scanner** was successfully implemented and tested using a controlled Dockerfile.

The scanner successfully identified three security configuration issues:

1. Unpinned `latest` base image tag.
2. SSH exposure on port `22`.
3. Missing explicit `USER` directive.

This task provided practical experience with Dockerfile static analysis and basic container security hardening concepts.

---
<a name="author-contact"></a>
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
```
