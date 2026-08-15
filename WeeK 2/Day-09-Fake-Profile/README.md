# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🔎 Day 9 — Social Media Impersonation & Fake Profile Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Type](https://img.shields.io/badge/Project-Fake%20Profile%20Detection-orange)
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
- [📊 Fake Profile Scoring](#-fake-profile-scoring)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🚀 How to Run](#-how-to-run)
- [📊 Output](#-output)
- [🛡️ Detection Indicators](#️-detection-indicators)
- [🔐 Ethical & Legal Notice](#-ethical--legal-notice)
- [📚 Learning Outcomes](#-learning-outcomes)
- [📈 Conclusion](#-conclusion)
- [👩‍💻 Author & Contact](#author-contact)
  
---

## 📌 Overview

Day 9 focuses on **Social Media Impersonation & Fake Profile Detection** in an authorized cybersecurity learning environment.

The project uses Python to evaluate social-media-style profile data and calculate a **fake-profile risk score** using behavioral heuristics.

The purpose is to understand common indicators associated with suspicious, fake, or bot-like profiles and improve social-engineering awareness.

---

## 🎯 Objective

To develop a Python-based fake-profile scorer that evaluates Twitter/X-like profile data using behavioral indicators and assigns a percentage-based risk score.

---

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Python Standard Library**
- **Command Prompt**
- **IDLE**
- **GitHub**

---

## 🔍 Methodology

```text
Profile Data
     ↓
Check Account Age
     ↓
Check Follower/Following Ratio
     ↓
Check Profile Picture
     ↓
Check Post Count
     ↓
Check Bio
     ↓
Calculate Fake Score
     ↓
Assign Risk Level
```
---

## 📊 Fake Profile Scoring

The scoring system evaluates several behavioral indicators:

| Indicator                         | Score |
| --------------------------------- | ----: |
| Account age below 30 days         |   +30 |
| Following/Follower ratio above 10 |   +25 |
| No profile picture                |   +20 |
| Less than 5 posts                 |   +15 |
| Default bio                       |   +10 |

The final score is limited to a maximum of **100%**.

### Risk Classification

|   Score | Risk Level  |
| ------: | ----------- |
|   0–29% | Low Risk    |
|  30–59% | Medium Risk |
| 60–100% | High Risk   |

---

## ⚙️ Features

* Calculates fake-profile risk score
* Evaluates account age
* Checks follower/following behavior
* Checks profile-picture availability
* Evaluates post activity
* Checks default bio indicators
* Assigns a risk level
* Uses fictional/anonymized profile data
* Runs locally without accessing real social-media accounts

---

## 📂 Project Structure

```text
Day-09-Fake-Profile/
│
├── fake_profile_detector.py
├── fake_profile_output.png
│
└── README.md
```

---

## 🚀 How to Run

### 1. Open the Project Directory

Open Command Prompt and navigate to the Day 9 folder:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-09-Fake-Profile
```

### 2. Run the Python Script

```bash
py fake_profile_detector.py
```

### 3. Review the Result

The program evaluates each profile and displays its fake-profile score and risk level.

---

## 📊 Output

Example output:

```text
Profile A -> Fake Score: 100% -> HIGH RISK
Profile B -> Fake Score: 0% -> LOW RISK
```

### Example Analysis

**Profile A**

* New account
* Very high following/follower ratio
* No profile picture
* Very few posts
* Default bio

**Result:**

```text
Fake Score: 100%
Risk: HIGH
```

**Profile B**

* Older account
* Established follower base
* Profile picture available
* Higher post activity
* Non-default bio

**Result:**

```text
Fake Score: 0%
Risk: LOW
```

---

## 🛡️ Detection Indicators

Common indicators that may help identify suspicious social-media profiles include:

* Very new accounts
* Unusual follower/following ratios
* Generic or default profile information
* Missing profile pictures
* Very low posting activity
* Similar or suspicious usernames
* Potentially cloned profile photos

These indicators should be treated as **risk signals rather than definitive proof** that an account is fake.

---

## 🔐 Ethical & Legal Notice

This project is intended for **authorized cybersecurity education, awareness training, and laboratory use only**.

* Fictional or anonymized profile data is used.
* No unauthorized social-media accounts were accessed.
* No account credentials were collected.
* No automated interaction with real social-media platforms was performed.
* The scoring system is a heuristic and should not be treated as definitive proof of impersonation.

---

## 📚 Learning Outcomes

Through this task, I learned:

* The concept of social-media impersonation
* Common characteristics of fake and bot-like profiles
* How behavioral heuristics can be used for risk scoring
* How Python can automate profile analysis
* How to assign risk levels based on multiple indicators
* The importance of social-engineering awareness

---

## 📈 Conclusion

The Day 9 project successfully demonstrates a Python-based heuristic approach to identifying potentially suspicious social-media profiles.

The project provides practical understanding of fake-profile indicators and shows how multiple behavioral signals can be combined into a simple risk score for cybersecurity awareness and analysis.

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
