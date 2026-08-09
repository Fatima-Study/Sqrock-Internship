# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 📧 Day 2 — Email Harvesting

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-Email%20Harvesting-success)
![Focus](https://img.shields.io/badge/Focus-Passive%20Reconnaissance-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Internship](https://img.shields.io/badge/Internship-SQROCK%20IT%20SOLUTION-blueviolet)

> A Python-based Email Harvesting Tool developed during Day 2 of the SQROCK IT SOLUTION Cybersecurity Internship to identify publicly visible email addresses from an authorized local practice webpage.

---

# 📑 Table of Contents

* Overview
* Objective
* Scope
* Tools and Technologies
* Methodology
* Project Structure
* Information Collected
* Key Insights
* Output
* How to Run This Project
* Security Relevance
* Ethical Considerations
* Limitations
* Future Work
* Conclusion
* Author & Contact

---

# 📌 Overview

Day 2 focused on understanding **Email Harvesting** as part of passive reconnaissance.

A Python-based Email Harvesting Tool was developed using the **Requests** library to retrieve webpage content and the **Regular Expressions (`re`)** module to identify email addresses.

An authorized local practice webpage containing dummy email addresses was used to safely demonstrate the email extraction process.

The scanner successfully identified **three dummy email addresses** from the practice webpage.

---

# 🎯 Objective

The objective of this project was to understand the concept of **email harvesting** and develop a Python-based tool to identify publicly visible email addresses from an authorized practice webpage.

The task provided practical experience with:

* Web content retrieval
* Python Requests library
* Regular expressions
* Email pattern matching
* Passive reconnaissance

---

# 🔐 Scope

The assessment was limited to an **authorized local practice webpage** created specifically for cybersecurity training.

The activity focused only on identifying email addresses present in the webpage source.

No unauthorized websites, systems, or personal information were targeted.

---

# 🛠️ Tools and Technologies

| Tool / Technology            | Purpose                                  |
| ---------------------------- | ---------------------------------------- |
| **Python**                   | Development of the Email Harvesting Tool |
| **Requests**                 | Retrieving webpage content               |
| **Regular Expressions (re)** | Identifying email address patterns       |
| **Local HTTP Server**        | Hosting the practice webpage             |
| **Command Prompt**           | Executing and testing the Python script  |

---

# 🔬 Methodology

The Email Harvesting Tool follows this workflow:

```text
┌───────────────────────────────┐
│ Authorized Practice Webpage  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Retrieve HTML using Requests  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Search Email Patterns using   │
│ Regular Expressions (Regex)   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Remove Duplicate Email        │
│ Addresses                     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Display Extracted Emails      │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Count Total Emails Found      │
└───────────────────────────────┘

---

### Process

1. Created an authorized local practice webpage containing dummy email addresses.
2. Hosted the webpage using a local Python HTTP server.
3. Used the `requests` library to retrieve the webpage content.
4. Applied a regular expression pattern to search for email addresses.
5. Removed duplicate email results.
6. Displayed the extracted email addresses and total count.
7. Verified the results through terminal output.

---

### 📂 Project Structure

```text
Day-2-Email-Harvesting/
│
├── email_harvesting.py
├── lab_page.html
├── Webpage.png
├── output.png
└── README.md
```

---

### 📊 Information Collected

The scanner identified publicly visible email addresses from the authorized practice webpage.

The collected information consisted only of **dummy email addresses created for the local cybersecurity training environment**.

### Information Extracted

* Email Address 1
* Email Address 2
* Email Address 3
* Total Number of Emails

---

# 💡 Key Insights

* Email addresses can be identified from publicly accessible webpage content.
* Regular expressions can automate email pattern detection.
* Python `requests` can retrieve webpage content for analysis.
* Duplicate email addresses can be removed during processing.
* Email harvesting can be part of passive reconnaissance.
* Publicly exposed contact information may increase an organization's reconnaissance footprint.

---

# 🖥️ Output

The Email Harvesting Tool successfully retrieved the authorized local practice webpage and identified **three dummy email addresses**.

### Sample Output

```text
========================================
 EMAIL HARVESTING TOOL
========================================

URL: http://localhost:8000/lab_page.html

Emails Found:
1. [Dummy Email 1]
2. [Dummy Email 2]
3. [Dummy Email 3]

Total Emails Found: 3

Email harvesting completed successfully.

---

# ▶️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Navigate to the Day 2 Folder

```bash
cd DecodeLabs-Internship/Day-2-Email-Harvesting
```

### 3. Install Required Library

```bash
pip install requests
```

### 4. Start the Local HTTP Server

Make sure `lab_page.html` is present in the project folder, then run:

```bash
python -m http.server 8000
```

### 5. Run the Email Harvesting Tool

Open another Command Prompt window and run:

```bash
python email_harvesting.py
```

### 6. View the Results

The program retrieves the authorized local webpage, identifies the email addresses, removes duplicates, and displays the total number of emails found.

---

# 🔎 Security Relevance

Email addresses can provide useful information during cybersecurity reconnaissance because they may reveal organizational contact points and potential targets for social engineering or phishing attempts.

Organizations should carefully consider what contact information is publicly exposed and apply appropriate security awareness measures.

---

# ⚖️ Ethical Considerations

This activity was performed in a **controlled and authorized cybersecurity training environment**.

* Only dummy email addresses were used.
* No real individuals were targeted.
* No unauthorized websites were accessed.
* No personal information was collected.
* The activity was limited to the authorized local practice environment.

---

# ⚠️ Limitations

1. The scanner only identifies email addresses present in the retrieved webpage content.
2. Dynamically generated emails may not be detected.
3. The regular expression may not match every possible email format.
4. Results depend on webpage availability and accessibility.
5. The assessment was limited to an authorized local practice environment.

---

# 🚀 Future Work

* Add support for scanning multiple authorized webpages.
* Improve email pattern detection.
* Add HTML report generation.
* Add duplicate and invalid email filtering.
* Integrate additional authorized OSINT sources.
* Develop a graphical user interface.

---

# ✅ Conclusion

The Day 2 task was successfully completed by developing and testing a Python-based **Email Harvesting Tool**.

The tool retrieved webpage content and successfully identified **three dummy email addresses using regular expressions**. The exercise demonstrated the basic role of email harvesting in passive reconnaissance and reinforced the importance of performing such activities only within an authorized environment.

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
