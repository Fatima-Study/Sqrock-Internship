# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🔎 Day 1 — OSINT & Passive Reconnaissance

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-OSINT%20Scanner-success)
![Focus](https://img.shields.io/badge/Focus-Passive%20Reconnaissance-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Internship](https://img.shields.io/badge/Internship-SQROCK%20IT%20SOLUTION-blueviolet)

> A Python-based OSINT Scanner developed during Day 1 of the SQROCK IT SOLUTION Cybersecurity Internship to collect publicly available information from an authorized practice domain.

---

# 📑 Table of Contents

* [Overview](#overview)
* [Objective](#objective)
* [Target Domain](#target-domain)
* [Tools and Technologies](#tools-and-technologies)
* [Methodology](#methodology)
* [Project Structure](#project-structure)
* [Information Collected](#information-collected)
* [Key Insights](#key-insights)
* [Output](#output)
* [How to Run This Project](#how-to-run-this-project)
* [Ethical Considerations](#ethical-considerations)
* [Limitations](#limitations)
* [Future Work](#future-work)
* [Conclusion](#conclusion)
* [Author & Contact](#author--contact)

---

# 📌 Overview

Day 1 focused on understanding **Open-Source Intelligence (OSINT)** and **Passive Reconnaissance** using Python.

A Python-based OSINT Scanner was developed to collect publicly available information from the authorized practice domain **example.com**. The scanner retrieves **WHOIS registrar information, the domain's IP address, and approximate IP geolocation data**.

This project provided practical experience in passive information gathering and demonstrated how publicly available information can support cybersecurity reconnaissance.

---

# 🎯 Objective

The objective of this project was to understand the fundamentals of **OSINT and passive reconnaissance** by developing a Python-based scanner capable of:

* Retrieving WHOIS information
* Resolving a domain name to an IP address
* Obtaining approximate IP geolocation
* Displaying the collected information

---

# 🌐 Target Domain

**Practice Domain:** `example.com`

The domain was selected as a practice domain for this authorized educational cybersecurity exercise.

---

# 🛠️ Tools and Technologies

| Tool / Technology  | Purpose                                    |
| ------------------ | ------------------------------------------ |
| Python             | Development of the OSINT Scanner           |
| Python-WHOIS       | Retrieving WHOIS registrar information     |
| Socket             | Resolving domain name to IP address        |
| Requests           | Sending API requests                       |
| IP Geolocation API | Obtaining approximate location information |

---

# 🔬 Methodology

The OSINT Scanner follows a passive reconnaissance workflow:

```text
User Enters Domain
        │
        ▼
Retrieve WHOIS Information
        │
        ▼
Resolve IP Address
        │
        ▼
Query IP Geolocation API
        │
        ▼
Display OSINT Results
        │
        ▼
Scan Completed Successfully
```

### Process

1. The authorized domain is provided to the scanner.
2. WHOIS information is retrieved to identify the registrar.
3. Python's `socket` module resolves the domain name to an IP address.
4. The IP address is submitted to an IP geolocation API.
5. Approximate city and country information are retrieved.
6. The collected information is displayed in the terminal.

---

# 📂 Project Structure

```text
Day-1-OSINT/
│
├── osint_scanner.py
│
├── output.png
│
└── README.md
```

---

# 📊 Information Collected

The OSINT Scanner collects the following publicly available information:

* **Domain Name**
* **WHOIS Registrar**
* **IP Address**
* **Approximate City**
* **Approximate Country**

---

# 💡 Key Insights

* OSINT can provide useful information through publicly available sources.
* WHOIS information can provide domain registrar details.
* DNS resolution can identify the IP address associated with a domain.
* IP geolocation can provide an approximate geographic location.
* Python can automate basic OSINT and passive reconnaissance tasks.
* Passive reconnaissance is an important initial step in cybersecurity analysis.

---

# 🖥️ Output

The Python OSINT Scanner successfully displayed the domain name, registrar, IP address, city, and country.

### Sample Output

```text
========================================
 OSINT SCANNER
========================================

Domain: example.com
Registrar: [WHOIS Registrar]
IP Address: [Resolved IP Address]
City: [Approximate City]
Country: [Approximate Country]

OSINT Scan Completed Successfully.
```
---

# ▶️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Navigate to the Day 1 Folder

```bash
cd DecodeLabs-Internship/Day-1-OSINT
```

### 3. Install Required Libraries

```bash
pip install python-whois requests
```

### 4. Run the Python Program

```bash
python osint_scanner.py
```

### 5. View the Results

The program will display the domain name, WHOIS registrar, IP address, approximate city, and country in the terminal.

---

# ⚖️ Ethical Considerations

This exercise was performed for **educational purposes** using an authorized practice domain.

* No real user was targeted.
* No company infrastructure was targeted.
* No unauthorized system was accessed.
* The activity was limited to passive collection of publicly available information.
* The exercise was performed within the authorized scope of the internship.

---

# ⚠️ Limitations

1. WHOIS information may be limited or privacy-protected.
2. IP geolocation provides only an approximate location.
3. DNS and IP information may change over time.
4. Results depend on the availability of external APIs.
5. The assessment was limited to passive information gathering.

---

# 🚀 Future Work

* Add subdomain enumeration.
* Add DNS record collection.
* Integrate additional OSINT APIs.
* Add automated report generation.
* Improve error handling and input validation.
* Develop a graphical user interface.

---

# ✅ Conclusion

The Day 1 task successfully demonstrated the basic concepts of **OSINT and passive reconnaissance using Python**. The developed scanner retrieved WHOIS, IP address, and approximate geolocation information, providing practical experience in collecting publicly available information for cybersecurity analysis.

---

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
</p>
