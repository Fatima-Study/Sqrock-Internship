# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🎯 Day 5 – GitHub Target Profile

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-GitHub%20Target%20Profile-002060)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-OSINT%20%7C%20Reconnaissance-orange)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A Python-based GitHub Target Profile tool that collects publicly available GitHub profile information and presents it in a structured format for basic OSINT and reconnaissance.

---

# 📑 Table of Contents

* [Overview](#overview)
* [Objective](#objective)
* [Problem Statement](#problem-statement)
* [Tools and Technologies](#tools-and-technologies)
* [Methodology](#methodology)
* [Information Collected](#information-collected)
* [Project Structure](#project-structure)
* [Key Insights](#key-insights)
* [Output](#output)
* [How to Run This Project](#how-to-run-this-project)
* [Security Relevance](#security-relevance)
* [Ethical Considerations](#ethical-considerations)
* [Limitations](#limitations)
* [Future Work](#future-work)
* [Conclusion](#conclusion)
* [Author & Contact](#author--contact)

---
<a name="overview"></a>
# 📌 Overview

The **GitHub Target Profile** is a Python-based OSINT project developed as part of **Day 5 of the Cybersecurity Internship**.

The tool collects publicly available information from a GitHub profile and presents it in a structured JSON format. The collected information can provide basic insights into a target's public GitHub presence.

The project was tested using a public GitHub profile and successfully generated a profile summary.

---
<a name="objective"></a>
# 🎯 Objective

The objective of this project is to understand how publicly available GitHub information can be collected and organized using Python for basic OSINT and reconnaissance purposes.

---
<a name="problem-statement"></a>
# 📝 Problem Statement

Public developer profiles can contain useful information such as names, organizations, locations, repositories, and programming languages.

This project provides a simple Python-based approach to collect selected publicly available GitHub profile information and organize it into a structured target profile.

---
<a name="tools--technologies"></a>
# 🛠️ Tools and Technologies

| Tool / Technology        | Purpose                                |
| ------------------------ | -------------------------------------- |
| **Python 3.x**           | Development of the GitHub profile tool |
| **GitHub**               | Public profile information source      |
| **JSON**                 | Structured profile data and output     |
| **Command Prompt (CMD)** | Program execution and testing          |
| **OSINT Techniques**     | Public information gathering           |

---
<a name="methodology"></a>
# ⚙️ Methodology

The tool follows these steps:

1. Define the GitHub target profile.
2. Retrieve publicly available profile information.
3. Extract selected profile details.
4. Identify the number of public repositories.
5. Analyze available programming language information.
6. Organize the collected information into JSON format.
7. Save the generated target profile.
8. Display the results in the Command Prompt.

---
<a name="information-collected"></a>
# 📊 Information Collected

The tool collects the following publicly available information:

* 👤 **Name**
* 🏢 **Company / Organization**
* 📍 **Location**
* 📂 **Number of Public Repositories**
* 💻 **Top Programming Languages**
* 📝 **Public Bio**

---
<a name="project-structure"></a>
# 📂 Project Structure

The Day 5 project contains the Python source code, output evidence, project documentation, and license file.

```text
Day-05-Target-Profile/
│
├── github_target_profile.py
├── output.png
└── README.md
```
---
<a name="file-description"></a>
### 📁 File Description

| File                       | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| `github_target_profile.py` | Python script for collecting GitHub target profile information |
| `output.png`               | Screenshot of the generated target profile output              |
| `README.md`                | Complete project documentation                                 |
| `LICENSE`                  | MIT License for the project                                    |

---
<a name="key-insights"></a>
# 💡 Key Insights

* Public GitHub profiles can provide useful information for OSINT.
* Repository counts can indicate a user's public development activity.
* Programming languages can provide insight into a developer's technical interests.
* Public profile information can support basic reconnaissance.
* OSINT information should be collected and used responsibly.

---
<a name="output"></a>
# 🖥️ Output

The tool was successfully tested using a public GitHub profile.

### Sample Output

```text
==================================================
              GITHUB TARGET PROFILE
==================================================

{
    "name": "Linus Torvalds",
    "company": "Linux Foundation",
    "location": "Portland, OR",
    "public_repos": 12,
    "top_langs": {
        "OpenSCAD": 1,
        "C": 8,
        "C++": 1
    },
    "bio": null
}

Profile JSON saved successfully.
```

---
<a name="how-to-run-this-project"></a>
# ▶️ How to Run This Project

### 1. Clone the Repository

Clone the DecodeLabs Internship repository:

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Navigate to the Project Folder

```bash
cd DecodeLabs-Internship/Day-05-Target-Profile
```

### 3. Run the Python Program

```bash
python github_target_profile.py
```

### 4. View the Results

The program will display the collected GitHub profile information and save the generated profile in JSON format.

---
<a name="security-relevance"></a>
# 🛡️ Security Relevance

Public developer information can contribute to the reconnaissance phase of cybersecurity assessments.

Understanding what information is publicly exposed helps security professionals identify potential information-disclosure risks and encourages users to review their public profiles carefully.

---
<a name="ethical-considerations"></a>
# 🔐 Ethical Considerations

This project is developed for **educational and authorized cybersecurity purposes only**.

Only publicly available information should be collected. The tool should not be used for harassment, unauthorized targeting, credential attacks, or other malicious activities.

---
<a name="limitations"></a>
# ⚠️ Limitations

* The tool only works with publicly available information.
* Profile information may be incomplete or unavailable.
* Public data can change over time.
* The tool does not access private repositories or private account information.
* The collected information should not be treated as a complete security profile.

---
<a name="future-work"></a>
# 🚀 Future Work

* Add GitHub repository analysis.
* Add contribution and activity analysis.
* Add organization and repository relationship mapping.
* Add automated JSON and PDF reporting.
* Add support for analyzing multiple authorized profiles.
* Integrate additional public OSINT sources.

---
<a name="conclusion"></a>
# ✅ Conclusion

The **GitHub Target Profile** project successfully demonstrated how Python can be used to collect and organize publicly available GitHub information.

The project provided practical experience in **OSINT, profile reconnaissance, JSON data handling, and cybersecurity information gathering**.

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
