# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🎯 Day 15 — SE Attack Chain Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Project](https://img.shields.io/badge/Project-Final%20Project-orange)
![CLI](https://img.shields.io/badge/Interface-CLI-purple)
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
- [🔗 Attack Chain](#attack-chain)
- [🧠 Key Concepts](#key-concepts)
- [🛠️ Tools & Technologies](#tools--technologies)
- [🔍 Methodology](#methodology)
- [⚙️ Features](#features)
- [📂 Project Structure](#project-structure)
- [🚀 How to Run](#how-to-run)
- [🖥️ CLI Modules](#cli-modules)
- [📊 Output](#output)
- [🛡️ Security & Awareness](#security--awareness)
- [🔐 Ethical & Legal Notice](#ethical--legal-notice)
- [📚 Learning Outcomes](#learning-outcomes)
- [📈 Conclusion](#conclusion)
- [👩‍💻 Author & Contact](#author-contact)
---

<a name="overview"></a>

## 📌 Overview

Day 15 is the **Final Project — SE Attack Chain Simulator**.

The project combines multiple cybersecurity concepts and modules into a single Python-based Command-Line Interface (CLI) tool.

The simulator provides separate modules for passive OSINT, target profile generation, phishing-risk scoring, phishing-awareness email templates, and incident-response simulation.

The project is designed for authorized cybersecurity education and laboratory environments.

---

<a name="objective"></a>

## 🎯 Objective

The objective of this project is to integrate multiple social-engineering security modules into one CLI-based simulator.

The tool demonstrates how different stages of a social-engineering attack chain can be analyzed from a defensive cybersecurity and awareness perspective.

---

<a name="attack-chain"></a>

## 🔗 Attack Chain

The project demonstrates the following conceptual attack chain:

```text
OSINT
  ↓
Profile Build
  ↓
Phishing Analysis
  ↓
Awareness Email Template
  ↓
Incident Response
```

The integrated CLI allows each module to be selected independently from the main menu.

---

<a name="key-concepts"></a>

## 🧠 Key Concepts

The project covers:

* OSINT
* Target Profiling
* Phishing Awareness
* Phishing Risk Scoring
* Social Engineering
* Incident Response
* Security Monitoring
* CLI-Based Security Tools

---

<a name="tools--technologies"></a>

## 🛠️ Tools & Technologies

* **Python 3.x**
* **Python Standard Library**
* **Command Line Interface (CLI)**
* **Regular Expressions**
* **JSON**
* **GitHub**

---

<a name="methodology"></a>

## 🔍 Methodology

```text
Start Simulator
      ↓
Display CLI Menu
      ↓
Select Security Module
      ↓
Run Selected Module
      ↓
Display Analysis / Simulation Result
      ↓
Return to Main Menu
      ↓
Select Another Module or Exit
```

---

<a name="features"></a>

## ⚙️ Features

The simulator provides the following modules:

* Passive OSINT simulation
* Sample target profile generation
* Phishing-risk scoring
* Phishing-awareness email template
* Incident-response simulation
* Interactive CLI menu
* Local execution
* Security-awareness focused output

---

<a name="project-structure"></a>

## 📂 Project Structure

```text
Day-15-SE-Chain-Simulator/
│
├── se_chain.py
├── module_output.txt
│
└── README.md
```

---

<a name="how-to-run"></a>

## 🚀 How to Run

### 1. Open Command Prompt

Navigate to the project folder:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-15-SE-Chain-Simulator
```

### 2. Run the Simulator

```bash
py se_chain.py
```

### 3. Select a Module

The program displays an interactive menu:

```text
============================================================
          SE CHAIN SIMULATOR
       SQROCK CYBERSECURITY INTERNSHIP
============================================================

 [osint] Run passive OSINT on a practice domain
 [profile] Build a sample target profile
 [phish] Score a URL for phishing indicators
 [template] Generate a phishing-awareness email
 [ir] Trigger incident response workflow
 [exit] Exit simulator

Select module:
```

---

<a name="cli-modules"></a>

## 🖥️ CLI Modules

### 🔎 OSINT Module

The OSINT module demonstrates passive information gathering using a practice domain.

```text
Practice Domain: example.com
Purpose: Passive information gathering
```

---

### 👤 Profile Module

The profile module creates a fictional laboratory target profile.

Example information includes:

* Name
* Role
* Technology stack
* Laboratory environment

---

### 🎣 Phishing Score Module

The phishing module performs a basic awareness-oriented URL risk assessment.

Example:

```text
URL: https://example.com
Phishing Risk Score: 0%
Purpose: Awareness training only.
```

---

### 📧 Email Template Module

The template module generates a phishing-awareness training email.

The generated content highlights common warning signs such as:

* Urgency
* Unexpected verification requests
* Suspicious links
* Requests for sensitive information

No real email is sent.

---

### 🛡️ Incident Response Module

The incident-response module simulates a high-severity phishing incident.

Example response actions include:

```text
[x] SIMULATION: Lock affected account
[x] SIMULATION: Revoke active sessions
[x] Notify SOC team
[x] Preserve security logs
[x] Quarantine suspicious email
```

The actions are simulated and do not affect real accounts or systems.

---

<a name="output"></a>

## 📊 Output

The program provides an interactive CLI interface and displays the selected module's result directly in the Command Prompt.

Example:

```text
--- INCIDENT RESPONSE MODULE ---

Incident Type : phishing
Severity      : HIGH

Response Actions:

[x] SIMULATION: Lock affected account
[x] SIMULATION: Revoke active sessions
[x] Notify SOC team
[x] Preserve security logs
[x] Quarantine suspicious email

Incident response simulation completed.
```

Screenshots of the CLI output are included in the `screenshots` folder.

---

<a name="security--awareness"></a>

## 🛡️ Security & Awareness

The project demonstrates how different stages of social engineering can be analyzed and how defensive controls can be applied.

Important defensive practices include:

* Security-awareness training
* Phishing detection
* Multi-factor authentication
* Monitoring suspicious login activity
* Incident-response planning
* Proper security logging
* Verification of unexpected requests

---

<a name="ethical--legal-notice"></a>

## 🔐 Ethical & Legal Notice

This project is strictly intended for **authorized cybersecurity education, research, and laboratory environments**.

* Only fictional laboratory data is used.
* No real users are targeted.
* No real phishing campaign is conducted.
* No real credentials are collected.
* No unauthorized systems are accessed.
* Incident-response actions are simulations only.
* The project must not be used for unauthorized attacks.

---

<a name="learning-outcomes"></a>

## 📚 Learning Outcomes

Through this final project, I learned:

* How cybersecurity modules can be integrated into one application
* Basics of CLI-based security tools
* Passive OSINT concepts
* Target profile generation
* Phishing-risk analysis
* Phishing-awareness content creation
* Incident-response workflows
* Security automation using Python
* Importance of ethical cybersecurity practices

---

<a name="conclusion"></a>

## 📈 Conclusion

The Day 15 project successfully integrates multiple cybersecurity and social-engineering awareness concepts into a single Python-based CLI simulator.

The project demonstrates a structured workflow from information gathering and profile analysis to phishing awareness and incident response.

This final project helped consolidate the practical Python and cybersecurity skills developed throughout the internship.

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
