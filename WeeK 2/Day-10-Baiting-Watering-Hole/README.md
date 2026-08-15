# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🎯 Day 10 — Baiting & Watering Hole Attack Simulation

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

- [📌 Overview](#overview)
- [🎯 Objective](#objective)
- [🛠️ Tools & Technologies](#tools--technologies)
- [🔍 Methodology](#methodology)
- [⚙️ Features](#features)
- [📂 Project Structure](#project-structure)
- [🚀 How to Run](#how-to-run)
- [📊 Output](#output)
- [🛡️ Prevention Measures](#prevention-measures)
- [🔐 Ethical & Legal Notice](#ethical--legal-notice)
- [📚 Learning Outcomes](#learning-outcomes)
- [📈 Conclusion](#conclusion)
- [👩‍💻 Author & Contact](#author-contact)

---
<a name="overview"></a>
## 📌 Overview

Day 10 focuses on **Baiting & Watering Hole Attack Simulation** in an authorized cybersecurity laboratory environment.

The project demonstrates a safe honeypot-style web server using Python. The local server records incoming requests and stores basic request information such as timestamp, IP address, requested path, and user-agent.

The simulation is designed to understand how suspicious links or web resources can be monitored in a controlled environment.

---
<a name="objective"></a>
## 🎯 Objective

To understand baiting and watering-hole attack concepts by creating a local Python-based honeypot that captures and logs simulated web requests for cybersecurity awareness and defensive analysis.

---
<a name="tools--technologies"></a>
## 🛠️ Tools & Technologies

- **Python 3.x**
- **Python Standard Library**
- **http.server**
- **BaseHTTPRequestHandler**
- **datetime**
- **json**
- **Command Prompt**
- **Localhost**
- **GitHub**

---
<a name="methodology"></a>
## 🔍 Methodology

```text
Create Local Honeypot Server
            ↓
Start Server on Localhost
            ↓
Create Simulated Bait Link
            ↓
Visit Link in Browser
            ↓
Capture Incoming Request
            ↓
Record Timestamp, IP, Path & User-Agent
            ↓
Save Log Information
            ↓
Analyze Security Implications
            ↓
Apply Defensive Measures
```
---
<a name="features"></a>
## ⚙️ Features

* Local honeypot web server
* Simulated bait-link interaction
* HTTP request monitoring
* Timestamp logging
* Client IP logging
* Requested path logging
* User-agent logging
* JSON-based log storage
* Localhost-only testing
* No external tracking

---
<a name="project-structure"></a>
## 📂 Project Structure

```text
Day-10-Baiting-Watering-Hole/
│
├── honeypot_tracker.py
├── honeypot_log-json.py
├── browser-test.png
|
├── honeypot-log-output.png
├── honeypot_server.txt
│
└── README.md
```

---
<a name="how-to-run"></a>
## 🚀 How to Run

### 1. Open the Project Directory

Open Command Prompt and navigate to the Day 10 folder:

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-10-Baiting-Watering-Hole
```

### 2. Start the Honeypot Server

Run:

```bash
py honeypot_tracker.py
```

The server starts at:

```text
http://localhost:8080
```

Expected output:

```text
Honeypot running on http://localhost:8080
```

### 3. Open the Simulated Bait Link

Open a browser and visit:

```text
http://localhost:8080
```

The server responds with:

```text
Thanks for visiting!
```

### 4. Test Additional Paths

The following local paths can also be tested:

```text
http://localhost:8080/download
http://localhost:8080/free-file
http://localhost:8080/update
```

### 5. Check the Log

The captured requests are stored in:

```text
honeypot_log.json
```

---
<a name="output"></a>
## 📊 Output

After visiting the local honeypot, the server captures request information.

Example:

```json
{
  "time": "2026-08-15 05:20:00",
  "ip": "127.0.0.1",
  "path": "/",
  "agent": "Mozilla/5.0"
}
```

The log records:

* Request timestamp
* Client IP address
* Requested URL path
* Browser/User-Agent information

Since the test is performed on localhost, the IP address appears as:

```text
127.0.0.1
```

---
<a name="prevention-measures"></a>
## 🛡️ Prevention Measures

Organizations can reduce the risks associated with baiting and watering-hole attacks through:

* **Web Filtering**
* **Script Blocking**
* **NoScript / Browser Security Controls**
* **Patch Management**
* Regular security awareness training
* Avoiding suspicious downloads and links
* Keeping browsers and applications updated

---
<a name="ethical--legal-notice"></a>
## 🔐 Ethical & Legal Notice

This project is strictly intended for **authorized cybersecurity education, awareness training, and laboratory testing**.

* The honeypot runs only on localhost.
* No real websites were targeted.
* No real users were tracked.
* No external systems were accessed.
* No malicious payload was delivered.
* The captured IP address belongs to the local test environment.
* The project must not be used to monitor or track users without authorization.

---
<a name="learning-outcomes"></a>
## 📚 Learning Outcomes

Through this task, I learned:

* The concept of baiting attacks
* The concept of watering-hole attacks
* How honeypots can be used for security monitoring
* How Python can create a simple local HTTP server
* How HTTP requests can be captured and logged
* How JSON can be used to store security logs
* The importance of web filtering and patch management

---
<a name="conclusion"></a>
## 📈 Conclusion

The Day 10 project successfully demonstrated a controlled baiting and watering-hole attack simulation using a Python-based local honeypot.

The project provided practical understanding of request monitoring and logging while maintaining a safe and isolated laboratory environment. It also highlighted defensive measures such as web filtering, script blocking, and patch management.

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
