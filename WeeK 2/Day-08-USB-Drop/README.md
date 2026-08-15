# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🔌 Day 8 — USB Drop Attack Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Type](https://img.shields.io/badge/Project-Security%20Awareness-orange)
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
- [🛡️ Prevention Measures](#️-prevention-measures)
- [🔐 Ethical & Legal Notice](#-ethical--legal-notice)
- [📚 Learning Outcomes](#-learning-outcomes)
- [📈 Conclusion](#-conclusion)
- [👩‍💻 Author & Contact](#author-contact)

---

## 📌 Overview

Day 8 focuses on **USB Drop Attack Simulation** in an authorized cybersecurity laboratory environment.

The project demonstrates a benign Python payload that simulates the type of basic system-information collection that could occur in a USB-drop scenario. The collected information is saved locally in a `recon_log.txt` file.

The simulation is designed for cybersecurity awareness and defensive learning without using an actual malicious payload.

---

## 🎯 Objective

To simulate a USB-drop attack scenario using a benign Python program that collects basic system information and saves the simulated reconnaissance results to a local output file.

---

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Python Standard Library**
- **Command Prompt**
- **Windows**
- **GitHub**

### Python Modules Used

- `platform`
- `socket`
- `datetime`
- `os`

---

## 🔍 Methodology

```text
Create Benign Python Payload
            ↓
Collect Basic System Information
            ↓
Retrieve Hostname & OS Details
            ↓
Record Timestamp & User Information
            ↓
Save Information to recon_log.txt
            ↓
Review Security Implications
            ↓
Apply USB-Drop Prevention Measures
```
---

## ⚙️ Features

* Simulates a USB-drop attack scenario
* Collects basic system information
* Records hostname and operating-system information
* Records timestamp and current working directory
* Saves results to `recon_log.txt`
* Runs locally in a controlled environment
* Does not send information to an external server

---

## 📂 Project Structure

```text
Day-08-USB-Drop/
│
├── usb_payload_sim.py
├── recon_log.txt
├── recon-data.png
│
└── README.md
```

---

## 🚀 How to Run

### 1. Open the Project Directory

Open Command Prompt and navigate to the Day 8 folder:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-08-USB-Drop
```

### 2. Run the Python Script

```bash
py usb_payload_sim.py
```

### 3. Check the Output

After successful execution, the program displays:

```text
[SIM] Recon data saved to recon_log.txt
```

A `recon_log.txt` file is created in the project directory.

---

## 📊 Output

The program generates a local `recon_log.txt` file containing basic system information collected during the simulation.

Example:

```text
timestamp: 2026-08-15 05:...
hostname: ...
os: Windows
version: ...
user: ...
cwd: C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-08-USB-Drop
```

The output demonstrates how a seemingly simple executable file from a removable device could potentially collect system information if executed by a user.

---

## 🛡️ Prevention Measures

Organizations can reduce the risks associated with USB-drop attacks through:

* **Disable AutoRun**
* **Endpoint DLP**
* **User Awareness Training**
* Restricting the use of unauthorized removable devices
* Monitoring removable-media activity
* Educating users not to execute unknown files from USB devices

---

## 🔐 Ethical & Legal Notice

This project is strictly intended for **authorized cybersecurity education, awareness training, and laboratory testing**.

* The payload is benign and used only for simulation.
* Testing was performed on a controlled local system.
* No external systems were targeted.
* No data was transmitted outside the local environment.
* No persistence or malicious functionality was implemented.
* Do not execute unknown payloads or files on systems without authorization.

---

## 📚 Learning Outcomes

Through this task, I learned:

* The concept of USB-drop attacks
* How removable media can be used in social-engineering scenarios
* How Python can collect basic system information
* How system information can be written to a local file
* The importance of USB security policies
* The role of endpoint protection and user awareness

---

## 📈 Conclusion

The Day 8 project successfully demonstrated a controlled USB-drop attack simulation using a benign Python payload.

The exercise provided practical understanding of how a suspicious file from removable media could collect basic system information and highlighted the importance of preventive controls such as disabling AutoRun, Endpoint DLP, and user awareness training.

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
