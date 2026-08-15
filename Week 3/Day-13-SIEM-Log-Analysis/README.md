# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🎯 Day 13 — SIEM Log Analysis for Social Engineering Attack Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![SIEM](https://img.shields.io/badge/Technology-SIEM-orange)
![Log Analysis](https://img.shields.io/badge/Focus-Log%20Analysis-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [📌 Overview](#overview)
- [🎯 Objective](#objective)
- [🧠 Key Concepts](#key-concepts)
- [🛠️ Tools & Technologies](#tools--technologies)
- [🔍 Methodology](#methodology)
- [⚙️ Features](#features)
- [📂 Project Structure](#project-structure)
- [🚀 How to Run](#how-to-run)
- [📊 Detection Results](#detection-results)
- [📄 Alert Report](#alert-report)
- [🛡️ Security Awareness](#security-awareness)
- [🔐 Ethical & Legal Notice](#ethical--legal-notice)
- [📚 Learning Outcomes](#learning-outcomes)
- [📈 Conclusion](#conclusion)
- [👩‍💻 Author & Contact](#author-contact)

---

<a name="overview"></a>

## 📌 Overview

Day 13 focuses on **SIEM Log Analysis for Social Engineering Attack Detection**.

The project uses Python to parse sample security logs and identify suspicious activities that may indicate security attacks or social-engineering-related anomalies.

The parser analyzes events such as repeated failed login attempts and suspicious email-rule creation and generates security alerts.

---

<a name="objective"></a>

## 🎯 Objective

The objective of this task is to develop a simple Python-based log-analysis tool that can:

- Parse security log entries
- Identify repeated failed login attempts
- Detect suspicious email-rule creation
- Generate security alerts
- Produce an alert summary report

---

<a name="key-concepts"></a>

## 🧠 Key Concepts

The project covers:

- SIEM
- Security Log Analysis
- Event Monitoring
- Brute-Force Detection
- Failed Login Analysis
- Email Rule Monitoring
- Security Alerts
- Social Engineering Detection

---

<a name="tools--technologies"></a>

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Python Standard Library**
- **Regular Expressions**
- **Collections / Counter**
- **Command Prompt**
- **GitHub**

---

<a name="methodology"></a>

## 🔍 Methodology

```text
Sample Security Logs
        ↓
Python Log Parser
        ↓
Extract Security Events
        ↓
Count Failed Login Attempts
        ↓
Detect Repeated Attempts
        ↓
Detect Suspicious Email Rules
        ↓
Generate Security Alerts
        ↓
Create Alert Summary
```
---

<a name="features"></a>

## ⚙️ Features

* Parses sample security logs
* Detects repeated failed login attempts
* Detects suspicious email-rule creation
* Generates automated alerts
* Counts security events
* Provides an analysis summary
* Generates a text-based alert report
* Runs locally using Python

---

<a name="project-structure"></a>

## 📂 Project Structure

```text
Day-13-SIEM-Log-Analysis/
│
├── siem_log_parser.py
|
├── alert_report.txt
├── siem_output.txt
│
└── README.md
```

---

<a name="how-to-run"></a>

## 🚀 How to Run

### 1. Open Command Prompt

Navigate to the Day 13 folder:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-13-SIEM-Log-Analysis
```

### 2. Run the Python Program

```bash
py siem_log_parser.py
```

---

<a name="detection-results"></a>

## 📊 Detection Results

The parser analyzes the sample security logs and generates alerts for suspicious activities.

Example output:

```text
============================================================
        SIEM LOG ANALYSIS
============================================================

Analyzing security logs...

[ALERT] Brute force detected: admin (3 failed attempts)
[ALERT] Suspicious email rule created by: admin

============================================================
ANALYSIS SUMMARY
============================================================
Failed login events: 3
Suspicious email rules: 1
Alerts generated: 2

Log analysis completed successfully!
```

### Detected Events

| Event                   | Detection                   |
| ----------------------- | --------------------------- |
| Repeated `FAILED_LOGIN` | Brute-force alert           |
| `EMAIL_RULE_CREATED`    | Suspicious email-rule alert |

---

<a name="alert-report"></a>

## 📄 Alert Report

The project includes:

```text
alert_report.txt
```

The report records the detected security events and summarizes the analysis.

Example:

```text
DAY 13 — SIEM LOG ANALYSIS REPORT

Project:
SIEM Log Analysis for Social Engineering Attack Detection

Log Source:
Provided Sample Security Logs

Detected Alerts:

1. Brute Force Detection
User: admin
Failed Attempts: 3

2. Suspicious Email Rule
User: admin
Event: EMAIL_RULE_CREATED
Rule: forward_all

Analysis:
The Python parser successfully analyzed the sample security logs
and identified repeated failed login attempts and a suspicious
email-rule creation event.

Status:
Analysis Completed Successfully.
```

---

<a name="security-awareness"></a>

## 🛡️ Security Awareness

Security logs can provide useful indicators of suspicious activity.

Important indicators include:

* Multiple failed login attempts
* Unusual login activity
* Suspicious account behavior
* Unexpected email-rule creation
* Unusual forwarding activity

Organizations can use centralized log monitoring and SIEM solutions to help detect and investigate suspicious events.

---

<a name="ethical--legal-notice"></a>

## 🔐 Ethical & Legal Notice

This project is strictly intended for **authorized cybersecurity education, research, and laboratory environments**.

* Only sample security logs were analyzed.
* No real user accounts were targeted.
* No unauthorized systems were accessed.
* No real credentials were collected.
* The project was executed locally for educational purposes.

---

<a name="learning-outcomes"></a>

## 📚 Learning Outcomes

Through this task, I learned:

* Basics of SIEM and security monitoring
* Security log analysis
* Python-based log parsing
* Regular expression usage
* Detection of repeated login failures
* Identification of suspicious email activity
* Automated alert generation
* Security event reporting

---

<a name="conclusion"></a>

## 📈 Conclusion

The Day 13 project successfully demonstrates a basic **SIEM log-analysis workflow using Python**.

The parser analyzes sample security events, identifies suspicious patterns, generates alerts, and produces an analysis report. This task provided practical experience with security monitoring and event-based threat detection.

---

<a name="author-contact"></a>

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  Cybersecurity | SQROCK IT SOLUTION — Internship
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">GitHub Profile</a> •
  <a href="https://www.linkedin.com/in/fatima-taufique-1313b633b/">LinkedIn</a>
</p>
