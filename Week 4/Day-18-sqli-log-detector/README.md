# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🔎 Day 18 — SQL Injection Log Detection Engine

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Regex](https://img.shields.io/badge/Detection-Regex-orange)
![Web Security](https://img.shields.io/badge/Focus-Web%20Security-red)
![SQL Injection](https://img.shields.io/badge/Threat-SQL%20Injection-critical)
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
- [Detection Signatures](#-detection-signatures)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Detection Summary](#-detection-summary)
- [SQL Injection Analysis](#️-sql-injection-analysis)
- [Secure SQL Practices](#-secure-sql-practices)
- [Recommendations](#-recommendations)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author--contact)

---

## 📌 Overview

This project implements a Python-based **SQL Injection Log Detection Engine** for identifying suspicious SQL injection patterns in controlled mock web access logs.

The detector uses **regular expressions (Regex)** and URL decoding to analyze log entries and classify them as either normal requests or potentially malicious SQL injection activity.

> ⚠️ **Safety Notice:** This project uses controlled mock logs for defensive security analysis. No real website or unauthorized system was targeted.

---

## 🎯 Objective

The main objectives of this task are:

- Analyze mock web access logs.
- Detect common SQL Injection indicators.
- Use Regex-based signatures for pattern detection.
- Decode URL-encoded request parameters.
- Identify the source IP associated with suspicious requests.
- Generate critical security alerts.
- Understand secure SQL query practices.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Regular Expressions (`re`)**
- **URL Decoding (`urllib.parse`)**
- **HTTP Access Logs**
- **Command Prompt**
- **Local / Mock Security Lab**

---

## 🔍 Detection Signatures

The detection engine checks for suspicious patterns commonly associated with SQL Injection attempts.

| Signature | Description |
|---|---|
| `'` | Single-quote based SQL manipulation indicator |
| `--` | SQL comment indicator |
| `#` | SQL comment indicator |
| `OR 1=1` | Common SQL injection logic pattern |
| `UNION SELECT` | Common SQL query manipulation pattern |

The analyzer also decodes URL-encoded characters before applying the detection logic.

---

## ⚙️ Methodology

```text
Create Mock Access Logs
          ↓
Load Logs into Python
          ↓
URL Decode Request Data
          ↓
Apply Regex SQLi Signatures
          ↓
Analyze Each Log Entry
          ↓
Identify Normal / Suspicious Request
          ↓
Extract Source IP
          ↓
Generate Security Alert
          ↓
Save Detection Output
```

---

## 💻 Implementation

The detection engine uses Python's built-in `re` module for pattern matching.

URL-encoded request data is decoded before analysis so that encoded SQL injection indicators can also be identified.

Example encoded input:

```text
%27%20OR%20%271%27=%271
```

After decoding:

```text
' OR '1'='1
```

The detector can then identify the SQL injection pattern.

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-18-sqli-log-detector
```

Run the detector:

```cmd
py log_detector.py
```

To save the detection output:

```cmd
py log_detector.py > output.txt
```

To view the saved output:

```cmd
type output.txt
```

---

## 📊 Testing and Results

The SQL Injection Log Detection Engine successfully analyzed the mock access logs.

### Actual Output

```text
[*] Starting SQL Injection Log Detection
------------------------------------------------------------

[NORMAL REQUEST] 192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200

[CRITICAL MALICIOUS PATTERN] Source: 10.0.4.12 -> String: 10.0.4.12 - "POST /auth/login?user=admin' OR '1'='1 HTTP/1.1" 401

[CRITICAL MALICIOUS PATTERN] Source: 172.16.5.9 -> String: 172.16.5.9 - "GET /search?q=UNION SELECT null,password FROM users-- HTTP/1.1" 500
```

---

## 📋 Detection Summary

| Source IP      | Request Type           | Detected Pattern      | Result           |
| -------------- | ---------------------- | --------------------- | ---------------- |
| `192.168.1.45` | Normal profile request | No SQLi signature     | ✅ Normal         |
| `10.0.4.12`    | Login request          | `' OR '1'='1`         | 🚨 SQLi Detected |
| `172.16.5.9`   | Search request         | `UNION SELECT` + `--` | 🚨 SQLi Detected |

### Overall Result

```text
Total Log Entries       : 3
Normal Requests         : 1
Suspicious Requests     : 2
SQLi Patterns Detected  : 2
```

---

## 🛡️ SQL Injection Analysis

**SQL Injection (SQLi)** is a web application security issue in which specially crafted input can alter the intended behavior of a database query.

For defensive monitoring, suspicious patterns in HTTP access logs can provide indicators that a request may contain SQL injection activity.

In this project, the following patterns were detected:

### 1. OR-Based SQL Injection

```text
' OR '1'='1
```

This type of input attempts to introduce a condition that evaluates as true.

### 2. UNION-Based SQL Injection

```text
UNION SELECT
```

This pattern may indicate an attempt to modify a query and retrieve additional database information.

### 3. SQL Comment Indicator

```text
--
```

SQL comment syntax can be used in injection payloads to alter how the remainder of a query is interpreted.

> Detection of a pattern in a log should be treated as a security indicator and investigated further. A pattern match alone does not prove that an application was successfully compromised.

---

## 🔐 Secure SQL Practices

A major defensive measure against SQL Injection is the use of **parameterized queries / prepared statements** instead of directly constructing SQL statements from user input.

### ❌ Unparameterized Approach

```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

In this approach, user-controlled input is directly combined with the SQL query.

### ✅ Parameterized Approach

```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

The parameterized approach keeps the SQL statement structure separate from user-provided data.

### Comparison

| Unparameterized SQL                        | Prepared Statements                         |
| ------------------------------------------ | ------------------------------------------- |
| User input may be directly concatenated    | User input is passed separately             |
| Higher SQL Injection risk                  | Stronger SQLi defense                       |
| Query structure can be influenced by input | Query structure remains separated from data |
| Not recommended                            | Recommended security practice               |

---

## 🔧 Recommendations

* Use parameterized queries or prepared statements.
* Avoid directly concatenating user input into SQL queries.
* Validate and appropriately handle application input.
* Monitor web access logs for suspicious SQLi indicators.
* Decode URL-encoded request parameters before security analysis.
* Investigate repeated suspicious requests from the same source.
* Use multiple security controls rather than relying only on log signatures.

---

## 📁 Project Structure

```text
Day-18-sqli-log-detector/
│
├── log_detector.py
├── output.png
|
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Python SQL Injection log detection.
* Mock HTTP access log analysis.
* URL decoding.
* Regex-based SQLi detection.
* Normal request identification.
* Suspicious request identification.
* Source IP extraction.
* Critical security alerts.
* Saved detection output.

### Screenshot

> **Figure 1: SQL Injection Log Detection Engine Output**

---

## ✅ Conclusion

The **SQL Injection Log Detection Engine** was successfully implemented and tested using controlled mock web access logs.

The analyzer successfully identified:

* `1` normal request.
* `2` suspicious requests.
* `OR '1'='1` SQL injection pattern.
* `UNION SELECT` SQL injection pattern.
* SQL comment indicator `--`.

The task demonstrated how Python-based Regex analysis can be used as a basic defensive mechanism for identifying potential SQL Injection indicators in web access logs.

---
<a name="author--contact"></a>
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
