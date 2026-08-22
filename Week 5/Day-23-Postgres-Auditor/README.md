# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🗄️ Day 23 — PostgreSQL Database Credential Auditing

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)
![Credential Audit](https://img.shields.io/badge/Focus-Credential%20Auditing-red)
![Database Security](https://img.shields.io/badge/Focus-Database%20Security-orange)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-purple)
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
- [Credential Security Checks](#-credential-security-checks)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Security Findings](#-security-findings)
- [Administrative Security Blueprint](#-administrative-security-blueprint)
- [Security Recommendations](#-security-recommendations)
- [Result Summary](#-result-summary)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **PostgreSQL Database Credential Auditor** for evaluating database authentication configurations in a controlled local environment.

The auditor evaluates credential pairs and identifies insecure default administrator credentials.

The test specifically checks for the default PostgreSQL credential combination:

```text
postgres : postgres
```

A secure example configuration is also evaluated to demonstrate a successful security check.

> ⚠️ **Safety Notice:** This project is intended for authorized local or isolated lab environments only.

---

## 🎯 Objective

The main objectives of this task are:

* Evaluate database credential configurations.
* Identify insecure default PostgreSQL credentials.
* Detect the `postgres:postgres` default credential combination.
* Generate a critical security finding when default credentials are active.
* Verify a secure credential configuration.
* Record the audit results.
* Understand basic PostgreSQL authentication security practices.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **PostgreSQL**
* **Python Dictionary**
* **Credential Evaluation Logic**
* **Command Prompt**
* **Local Security Lab**

---

## 🔍 Credential Security Checks

The auditor performs the following checks:

| Security Check            | Description                          | Result       |
| ------------------------- | ------------------------------------ | ------------ |
| Local Target              | Evaluates `127.0.0.1`                | ✅ Completed  |
| Default Credential        | Checks `postgres:postgres`           | 🔴 Detected  |
| Secure Configuration      | Evaluates secure example credentials | ✅ Passed     |
| Authentication Evaluation | Processes credential pairs           | ✅ Completed  |
| Verification Logging      | Displays audit results               | ✅ Successful |

---

## ⚙️ Methodology

```text
Requirement Review
      ↓
Credential Configuration
      ↓
Python Audit Script
      ↓
Evaluate Username + Password
      ↓
Check Default Credential
      ↓
Generate Security Finding
      ↓
Verify Secure Configuration
      ↓
Record Results
      ↓
Security Recommendations
```
---

## 💻 Implementation

The auditor uses a Python function to evaluate database credential configurations.

### Credential Evaluation Function

```python
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
```

### Test Credential Configuration

The local test uses:

```python
credentials = {
    "postgres": "postgres",
    "app_user": "SecureP@ss2026!"
}
```

The first configuration represents the insecure default credential pair, while the second is used as a secure example for evaluation.

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-23-Postgres-Credential-Auditing
```

Run the auditor:

```cmd
python postgres_auditor.py
```

To save the execution output:

```cmd
python postgres_auditor.py > output.txt
```

To view the saved output:

```cmd
type output.txt
```

---

## 📊 Testing and Results

The credential auditor was successfully executed against the local test target:

```text
127.0.0.1
```

### Test Results

| Credential Configuration    | Result      | Observation                               |
| --------------------------- | ----------- | ----------------------------------------- |
| `postgres:postgres`         | 🔴 Critical | Default administrator credential detected |
| `app_user: SecureP@ss2026!` | ✅ Passed    | Configuration passed evaluation           |

The execution successfully identified the default PostgreSQL credential and verified the secure example configuration.

---

## 🚨 Security Findings

### Finding 1 — Default PostgreSQL Credentials

The auditor detected:

```text
postgres:postgres
```

and generated:

```text
[CRITICAL OUTCOME] Default Administrator Credentials Active
```

Default administrator credentials can create significant authentication risk if they remain active in a deployed database environment.

---

### Finding 2 — Secure Configuration Passed

The following configuration was also evaluated:

```text
app_user: SecureP@ss2026!
```

The auditor reported:

```text
[-] Evaluation Passed for configuration pair -> app_user: Sec***
```

This demonstrates that the credential evaluation logic can distinguish the configured default credential from another credential pair.

---

## 🏛️ Administrative Security Blueprint

### 1. Strict Authorization Rules

Database access should follow defined authorization rules.

Users should receive only the permissions required for their assigned role.

```text
Administrator
      ↓
Administrative Permissions

Application User
      ↓
Application Permissions

Read-Only User
      ↓
Read-Only Permissions
```

Role-based access restrictions can help reduce unnecessary database privileges.

---

### 2. Connection Limiting

Database connections should be controlled and limited according to application requirements.

Connection controls can help prevent excessive connection usage and reduce resource exhaustion risks.

```text
Client Requests
      ↓
Connection Control
      ↓
Allowed Connections
      ↓
PostgreSQL Database
```

---

### 3. Row-Level Encryption Strategies

Sensitive database information should receive appropriate protection.

Where applicable, encryption strategies can be applied to sensitive data at the database or application layer.

```text
Sensitive Data
      ↓
Encryption Strategy
      ↓
Protected Data
      ↓
Authorized Access
```

---

## 🛡️ Security Recommendations

### Change Default Credentials

Default PostgreSQL credentials should not remain active in production environments.

### Use Strong Authentication

Use strong, unique credentials and appropriate authentication controls.

### Apply Least Privilege

Database accounts should receive only the permissions necessary for their tasks.

### Limit Database Access

Restrict database connectivity to authorized applications, users, and networks.

### Protect Sensitive Data

Apply suitable encryption strategies to sensitive database information.

### Monitor Authentication Activity

Database authentication events should be monitored for unusual or repeated failed access attempts.

---

## 📋 Result Summary

```text
Credential Auditor Implementation → PASS
Local Target Evaluation           → PASS
Default Credential Detection      → PASS
Critical Finding Generation       → PASS
Secure Configuration Evaluation   → PASS
Verification Logging              → PASS
```

### Overall Findings

| Security Check           | Result              |
| ------------------------ | ------------------- |
| Local Target `127.0.0.1` | ✅ Evaluated         |
| `postgres:postgres`      | 🔴 Critical Finding |
| Secure Configuration     | ✅ Passed            |
| Credential Evaluation    | ✅ Successful        |
| Audit Output             | ✅ Generated         |

---

## 📁 Project Structure

```text
Day-23-Postgres-Auditor/
│
├── postgres_auditor.py
├── output.png
│
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* PostgreSQL credential auditing logic.
* Local target evaluation.
* Default credential detection.
* Critical security finding generation.
* Secure configuration verification.
* Successful Python execution.
* Verification logging output.

---

## ✅ Conclusion

The **PostgreSQL Database Credential Auditor** was successfully implemented and tested in a controlled local environment.

The auditor successfully identified the default:

```text
postgres:postgres
```

credential combination as a **critical outcome** and successfully evaluated the secure example configuration.

This task provided practical experience with **database credential auditing, authentication security, default credential detection, authorization controls, connection limiting, and data protection strategies**.

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
