# 🔐 Day 3 – Phishing URL Risk Detector

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-Phishing%20URL%20Detector-002060)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Phishing%20Detection-orange)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A Python-based Phishing URL Risk Detector that analyzes URLs using predefined suspicious indicators and classifies them as Low, Medium, or High Risk.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Objective](#objective)
- [Problem Statement](#problem-statement)
- [Tools and Technologies](#tools-and-technologies)
- [Methods](#methods)
- [Detection Rules](#detection-rules)
- [Risk Classification](#risk-classification)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Output](#output)
- [How to Run This Project](#how-to-run-this-project)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Ethical Use](#ethical-use)
- [Learning Outcomes](#learning-outcomes)
- [Author & Contact](#author-contact)


---
<a name="overview"></a>
# 📌 Overview

The **Phishing URL Risk Detector** is a Python-based cybersecurity project developed as part of **Day 3 of the Cybersecurity Internship**.

The tool analyzes URLs for common suspicious characteristics associated with phishing attempts. It calculates a risk score based on detected indicators and classifies each URL as **Low, Medium, or High Risk**.

The detector was tested using multiple sample URLs to verify that different suspicious characteristics produced different risk levels.

---
<a name="objective"></a>
# 🎯 Objective

The objective of this project is to understand common characteristics of phishing URLs and develop a simple rule-based Python tool that can identify suspicious indicators and assign an appropriate risk level.

---
<a name="problem-statement"></a>
# 📝 Problem Statement

Phishing attacks often use deceptive URLs to trick users into visiting malicious websites or providing sensitive information.

A URL can contain several warning signs, such as the absence of HTTPS, suspicious keywords, excessive subdomains, or the use of an IP address instead of a domain name.

This project provides a simple automated approach for identifying these indicators and generating a risk score.

---
<a name="tools-and-technologies"></a>
# 🛠️ Tools and Technologies

| Tool / Technology           | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| **Python 3.x**              | Development of the phishing URL detector |
| **Python Standard Library** | URL parsing and pattern detection        |
| **Command Prompt (CMD)**    | Program execution and testing            |
| **Rule-Based Analysis**     | Phishing indicator detection             |

---
<a name="methods"></a>
# ⚙️ Methods

The detector follows these steps:

1. Accept a URL as input.
2. Parse and analyze the URL.
3. Check predefined suspicious indicators.
4. Assign points for each detected indicator.
5. Calculate the final risk score.
6. Cap the score at 100%.
7. Classify the URL as Low, Medium, or High Risk.
8. Display the detected indicators and final result.

---
<a name="detection-rules"></a>
# 🚨 Detection Rules

| Suspicious Indicator    |                    Score |
| ----------------------- | -----------------------: |
| **No HTTPS**            |                      +30 |
| **Suspicious Keyword**  | +20 per matching keyword |
| **Too Many Subdomains** |                      +25 |
| **IP Address in URL**   |                      +40 |

### Suspicious Keywords

The detector checks for keywords such as:

```text
login
verify
secure
update
account
bank
paypal
```
---
<a name="risk-classification"></a>
## 📊 Risk Classification

| Risk Level         |   Score |
| ------------------ | ------: |
| 🟢 **Low Risk**    |   0–39% |
| 🟡 **Medium Risk** |  40–69% |
| 🔴 **High Risk**   | 70–100% |

A **0% score** means that none of the implemented suspicious indicators were detected.

---
<a name="project-structure"></a>
# 📂 Project Structure

The Day 3 project contains the Python source code, testing evidence, and project documentation.
```text
Day-03-Phishing-URL-Detector/
│
├── url_detector.py
├── output_1.png
├── output_2.png
└── README.md
```
---

# File Description

| File                         | Description                               |
| ---------------------------- | ----------------------------------------- |
| **phishing_url_detector.py** | Main Python phishing URL risk detector    |
| **day3_phishing_output.png** | Screenshot showing the program output     |
| **day3_phishing_code.png**   | Screenshot showing the Python source code |
| **README.md**                | Complete project documentation            |

---
<a name="key-insights"></a>
# 💡 Key Insights

* Phishing URLs can contain multiple suspicious characteristics.
* The absence of HTTPS can increase the calculated risk score.
* Suspicious keywords may indicate attempts to imitate trusted services.
* IP addresses can be a warning sign when used instead of normal domain names.
* Multiple indicators can accumulate and produce a higher risk score.
* Rule-based detection provides a simple approach for cybersecurity awareness.

---
<a name="output"></a>
# 🖥️ Output

The detector was tested using **10 sample URLs**.

The program successfully generated risk scores and corresponding risk classifications.

### Test Results

* **3 URLs** received **High Risk – 70%**
* **3 URLs** received **Medium Risk – 40%**
* **4 URLs** received **Low Risk**

URLs containing multiple suspicious indicators received higher scores.

---
<a name="how-to-run-this-project"></a>
# ▶️ How to Run This Project

### 1. Clone the Repository

Clone the DecodeLabs Internship repository from GitHub.

### 2. Navigate to the Project Folder

Open Command Prompt and navigate to:

**Day-03-Phishing-URL-Detector**

### 3. Run the Python Program

Run the following command:

**python phishing_url_detector.py**

### 4. View the Results

Enter the sample URLs when prompted. The program will display the:

* Risk Score
* Risk Level
* Detected Indicators

---
<a name="limitations"></a>
# ⚠️ Limitations

* The detector uses predefined rules rather than machine learning.
* It cannot guarantee that a URL is completely safe or malicious.
* New phishing techniques may not be detected.
* Suspicious keywords can sometimes appear in legitimate URLs.
* The tool is intended for basic analysis and cybersecurity awareness.

---
<a name="future-work"></a>
# 🚀 Future Work

* Add machine-learning-based URL classification.
* Add domain reputation checking.
* Integrate threat-intelligence APIs.
* Add WHOIS and DNS analysis.
* Develop a graphical user interface.
* Add a larger and more diverse URL dataset.

---
<a name="ethical-use"></a>
# 🔐 Ethical Use

This project is developed for **educational and authorized cybersecurity purposes only**.

The detector should be used for security awareness, testing, and analysis of authorized or sample URLs. It should not be used to facilitate phishing campaigns or other malicious activities.

---
<a name="learning-outcomes"></a>
# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Understanding phishing URL characteristics.
* Developing rule-based security detection logic.
* Working with Python URL analysis.
* Implementing risk scoring.
* Classifying security risks.
* Testing cybersecurity detection tools.
* Documenting security projects professionally.

---
<a name="author-contact"></a>
# 👩‍💻 Author & Contact

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
