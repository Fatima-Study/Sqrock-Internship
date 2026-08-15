# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🔐 Day 7 — Password Attacks & Credential Stuffing

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Local%20Lab-black?logo=flask)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Type](https://img.shields.io/badge/Project-Security%20Simulation-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Objective](#-objective)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [🔍 Methodology](#-methodology)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🚀 How to Run](#-how-to-run)
- [📊 Output](#-output)
- [🛡️ Defensive Measures](#-defensive-measures)
- [🔐 Ethical & Legal Notice](#-ethical--legal-notice)
- [📚 Learning Outcomes](#-learning-outcomes)
- [📈 Conclusion](#-conclusion)
- [👩‍💻 Author & Contact](#author-contact)

---

## 📌 Overview

Day 7 focuses on **Password Attacks & Credential Stuffing** in an authorized local laboratory environment.

The project demonstrates the basic logic of password-guessing attempts against a **local Flask test server**. A Python simulator tests a small predefined wordlist against the local login endpoint and identifies the correct lab password.

The task also introduces defensive techniques such as **rate limiting, account lockout, CAPTCHA, MFA, and breach monitoring**.

---

## 🎯 Objective

To understand brute-force and credential-stuffing concepts by building a controlled Python login simulation against a local Flask test server and demonstrating defensive rate-limiting concepts.

---

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Flask**
- **Requests**
- **Command Prompt**
- **Localhost / 127.0.0.1**
- **GitHub**

---

## 🔍 Methodology

```text
Create Local Flask Login Server
            ↓
Define Lab Username & Password
            ↓
Create Test Password Wordlist
            ↓
Send Login Attempts
            ↓
Check Server Response
            ↓
Identify Failed Attempts
            ↓
Identify Successful Login
            ↓
Apply Defensive Rate Limiting
```
---

## ⚙️ Features

* Local Flask login server
* Controlled password-attempt simulation
* Small predefined password wordlist
* HTTP POST login requests
* Failed and successful attempt detection
* Localhost-only testing
* Defensive security awareness

---

## 📂 Project Structure

```text
Day-07-Password-Attack/
│
├── app.py
├── brute_force_simulator.py
├── flask_server.png
├── bruteforce_output.png
│
└── README.md
```

---

## 🚀 How to Run

### 1. Install Required Packages

Open Command Prompt and run:

```bash
py -m pip install flask requests
```

### 2. Start the Flask Server

Run:

```bash
py app.py
```

The local server will start at:

```text
http://127.0.0.1:5000
```

### 3. Open a Second Command Prompt

Navigate to the project directory:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-07-Pass-Attack
```

### 4. Run the Simulator

```bash
py brute_force_simulator.py
```

The simulator will test the predefined lab password list against the local Flask server.

---

## 📊 Output

The simulator produced the following result:

```text
[-] Failed: 123456
[-] Failed: password
[-] Failed: admin
[-] Failed: letmein
[+] PASSWORD FOUND: password123
```

The Flask server recorded unsuccessful login attempts with HTTP status `401` and the successful login with HTTP status `200`.

### Result

The controlled local simulation successfully demonstrated:

* Multiple failed login attempts
* Detection of the correct lab password
* HTTP response-based result checking
* Interaction between the Python simulator and Flask server

---

## 🛡️ Defensive Measures

Brute-force and credential-stuffing attacks can be reduced through:

* **Rate Limiting**
* **Account Lockout**
* **CAPTCHA**
* **Multi-Factor Authentication (MFA)**
* **Strong Password Policies**
* **Breach Monitoring**
* Monitoring repeated failed login attempts

A rate limiter can restrict repeated login requests after a defined number of failed attempts.

---

## 🔐 Ethical & Legal Notice

This project is strictly intended for **authorized cybersecurity education and local laboratory testing**.

* Testing was performed only against `127.0.0.1`.
* No real website or online account was targeted.
* No real user credentials were used.
* The password list contains only laboratory test values.
* The simulator must not be used against systems without explicit authorization.

---

## 📚 Learning Outcomes

Through this task, I learned:

* The basic concept of brute-force attacks
* The concept of credential stuffing
* How login requests work with HTTP POST
* How Flask can be used to create a local security-testing environment
* How Python can automate controlled login attempts
* How HTTP status codes can indicate login results
* The importance of rate limiting and MFA for defense

---

## 📈 Conclusion

The Day 7 project successfully demonstrated a controlled password-attack simulation using Python and a local Flask server.

The exercise provided practical understanding of password-guessing behavior while emphasizing defensive measures such as rate limiting, account lockout, CAPTCHA, and MFA.

---

<a name="author-contact"></a>

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  Cybersecurity | SQROCK IT SOLUTION — Internship (Aug-Sep 2026 Batch)
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">GitHub Profile</a> •
  <a href="https://www.linkedin.com/in/fatima-taufique-1313b633b/">LinkedIn</a>
</p>
