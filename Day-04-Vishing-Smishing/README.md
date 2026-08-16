# 📞 Day 4 – Vishing & Smishing Awareness

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-Vishing%20%26%20Smishing%20Awareness-002060)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Social%20Engineering-orange)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A Python-based Vishing Awareness Script Generator that creates security awareness scenarios for identifying and responding safely to suspicious phone calls and social-engineering attempts.

---

# 📑 Table of Contents

* [Overview](#overview)
* [Objective](#objective)
* [Problem Statement](#problem-statement)
* [Tools and Technologies](#tools-and-technologies)
* [Methodology](#methodology)
* [Awareness Scenarios](#awareness-scenarios)
* [Project Structure](#project-structure)
* [Key Insights](#key-insights)
* [Output](#output)
* [How to Run This Project](#how-to-run-this-project)
* [Security Relevance](#security-relevance)
* [Ethical Considerations](#ethical-considerations)
* [Limitations](#limitations)
* [Future Work](#future-work)
* [Conclusion](#conclusion)
* [Author & Contact](#author-contact)

---
<a name="overview"></a>
# 📌 Overview

The **Vishing & Smishing Awareness** project is a Python-based cybersecurity awareness project developed as part of **Day 4 of the Cybersecurity Internship**.

The project focuses on **vishing awareness** by generating realistic but safe awareness scripts that demonstrate how attackers may use impersonation, urgency, and social engineering techniques to influence users.

The generated scripts provide examples of suspicious situations along with common red flags and appropriate safety guidance.

---
<a name="objective"></a>
# 🎯 Objective

The objective of this project is to understand common social-engineering techniques used in vishing and improve cybersecurity awareness by generating safe training scenarios that demonstrate how users can identify and respond to suspicious calls.

---
<a name="problem-statement"></a>
# 📝 Problem Statement

Social-engineering attacks can manipulate users into revealing sensitive information or performing unsafe actions.

Vishing attacks may involve attackers impersonating IT support staff, bank officers, or government representatives and creating a sense of urgency.

This project provides awareness scripts that help users recognize common warning signs and follow safer verification practices.

---
<a name="tools-and-technologies"></a>
# 🛠️ Tools and Technologies

| Tool / Technology                | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| **Python 3.x**                   | Development of the awareness script generator |
| **Python Standard Library**      | Script generation and processing              |
| **Command Prompt (CMD)**         | Program execution and testing                 |
| **Social Engineering Awareness** | Understanding common vishing techniques       |

---

# ⚙️ Methodology

The script generator follows these steps:

1. Define an awareness scenario.
2. Specify the target organization.
3. Define the caller role.
4. Define the social-engineering pretext.
5. Generate an opening statement.
6. Generate a suspicious hook.
7. Identify common red flags.
8. Provide a security awareness message.
9. Display the generated awareness script.

---
<a name="awareness-scenarios"></a>
# 📞 Awareness Scenarios

The program successfully generated three awareness scripts.

### Script 1 – Password Reset

**Target Organization:** Training Lab
**Caller Role:** IT Support
**Pretext:** Password Reset

The caller claims that the user's account requires an urgent security reset.

**Red Flags:**

* Legitimate staff will never ask for your password.
* Never share OTPs or verification codes.
* Verify the caller through official channels.
* Do not act under pressure or urgency.

**Awareness Message:**

Stop the call and independently verify the request before sharing any information.

---

### Script 2 – Suspicious Transaction

**Target Organization:** Training Bank
**Caller Role:** Bank Security Officer
**Pretext:** Suspicious Transaction

The caller claims that unusual account activity has been detected and asks the user to verify the account.

**Red Flags:**

* Legitimate staff will never ask for your password.
* Never share OTPs or verification codes.
* Verify the caller through official channels.
* Do not act under pressure or urgency.

**Awareness Message:**

Stop the call and independently verify the request before sharing any information.

---

### Script 3 – Document Verification

**Target Organization:** Government Training Lab
**Caller Role:** Government Officer
**Pretext:** Document Verification

The caller claims that an important document requires immediate verification.

**Red Flags:**

* Legitimate staff will never ask for your password.
* Never share OTPs or verification codes.
* Verify the caller through official channels.
* Do not act under pressure or urgency.

**Awareness Message:**

Stop the call and independently verify the request before sharing any information.

---
<a name="project-structure"></a>
# 📂 Project Structure

The Day 4 project contains the Python source code, output evidence, project documentation, and license file.

```text
Day-04-Vishing-Smishing/
│
├── Code.py
├── Script-1.png
├── Script-2.png
├── Script-3.png
└── README.md
```
---
<a name="file-description"></a>
### 📁 File Description

| File                     | Description                                         |
| ------------------------ | --------------------------------------------------- |
| `se_script_generator.py` | Python-based vishing awareness script generator     |
| `output_1.png`           | Screenshot of the first generated awareness script  |
| `output_2.png`           | Screenshot of the second generated awareness script |
| `output_3.png`           | Screenshot of the third generated awareness script  |
| `README.md`              | Complete project documentation                      |
| `LICENSE`                | MIT License for the project                         |

---
<a name="key-insights"></a>
# 💡 Key Insights

* Vishing attacks often rely on impersonation and urgency.
* Attackers may pretend to be trusted employees or officials.
* Passwords and OTPs should never be shared over unsolicited calls.
* Users should independently verify suspicious requests.
* Awareness training can help users recognize social-engineering red flags.
* Avoiding pressure-based decisions can reduce the risk of social-engineering attacks.

---
<a name="output"></a>
# 🖥️ Output

The program successfully generated **three vishing awareness scripts** covering:

1. Password Reset
2. Suspicious Transaction
3. Document Verification

Each script included an **opener, hook, red flags, and awareness message**.

---
<a name="how-to-run-this-project"></a>
# ▶️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Navigate to the Project Folder

```bash
cd DecodeLabs-Internship/Day-04-Vishing-Smishing
```

### 3. Run the Python Program

```bash
python se_script_generator.py
```

### 4. View the Generated Scripts

The program will generate and display multiple awareness scenarios containing the caller role, pretext, hook, red flags, and awareness message.

---
<a name="security-relevance"></a>
# 🛡️ Security Relevance

Vishing is a form of social engineering that uses voice communication to manipulate victims.
This project demonstrates common warning signs and provides practical awareness messages that can help users identify suspicious calls and avoid sharing sensitive information.

---
<a name="ethical-considerations"></a>
# 🔐 Ethical Considerations

This project is developed strictly for **educational and cybersecurity awareness purposes**.

The generated scenarios are intended for training and awareness. They should not be used to impersonate real organizations, deceive individuals, or conduct real-world social-engineering attacks.

---
<a name="limitations"></a>
# ⚠️ Limitations

* The project generates predefined awareness scenarios.
* It does not detect real-time vishing or smishing attacks.
* Generated scenarios may not represent every possible social-engineering technique.
* The project does not analyze actual phone calls or SMS messages.
* Effectiveness depends on user awareness and proper security practices.

---
<a name="future-work"></a>
# 🚀 Future Work

* Add customizable awareness scenarios.
* Add smishing-specific SMS awareness examples.
* Add more social-engineering scenarios.
* Add an interactive awareness-training interface.
* Add quizzes for evaluating user awareness.
* Generate automated awareness reports.

---
<a name="conclusion"></a>
# ✅ Conclusion

The **Vishing & Smishing Awareness** project successfully demonstrated how Python can be used to generate cybersecurity awareness scenarios.

The project highlights common social-engineering red flags such as impersonation, urgency, and requests for sensitive information, helping users develop safer responses to suspicious communications.

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
