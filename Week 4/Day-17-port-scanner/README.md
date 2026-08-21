# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🌐 Day 17 — Local Network Port & Service Scanning

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Socket](https://img.shields.io/badge/Module-Socket-orange)
![Network](https://img.shields.io/badge/Focus-Network%20Security-red)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

</p>

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Objective](#-objective)
- [Technologies Used](#️-technologies-used)
- [Target and Ports](#-target-and-ports)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Result Summary](#-result-summary)
- [Network Topology](#-network-topology)
- [Security Analysis](#️-security-analysis)
- [Recommendations](#-recommendations)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a simple Python-based **Local Network Port and Service Scanner** for checking the availability of selected TCP ports on the local host.

The scan was performed in an authorized and controlled local environment using:

```text
127.0.0.1
```

The scanner uses Python's `socket` module to determine whether the selected ports are open or closed.

> ⚠️ **Safety Notice:** This project is intended for authorized local or isolated lab environments only.

---

## 🎯 Objective

The main objectives of this task are:

* Scan selected TCP ports on the local host.
* Identify whether ports are open or closed.
* Understand basic socket-based port scanning.
* Verify local service availability.
* Generate a port scanning output log.
* Create a simple network mapping topology.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Socket Module**
* **TCP**
* **Command Prompt**
* **Localhost / Loopback Interface**

---

## 🔍 Target and Ports

### Target

```text
127.0.0.1
```

### Ports Tested

| Port   | Common Service        |
| ------ | --------------------- |
| `22`   | SSH                   |
| `80`   | HTTP                  |
| `443`  | HTTPS                 |
| `5432` | PostgreSQL            |
| `8080` | Alternate Web / Proxy |

---

## ⚙️ Methodology

```text
Start
  ↓
Select Localhost 127.0.0.1
  ↓
Select Target Ports
  ↓
Create TCP Socket
  ↓
Attempt Connection
  ↓
Check Connection Result
  ↓
Identify OPEN / CLOSED Port
  ↓
Display Results
  ↓
Save Output
  ↓
Complete Network Mapping
```

---

## 💻 Implementation

The scanner uses Python's built-in `socket` module.

The `connect_ex()` function is used to attempt a TCP connection to each selected port.

A successful connection indicates an **OPEN** port, while a failed connection indicates a **CLOSED** port.

The scanner checks:

```text
22
80
443
5432
8080
```

on:

```text
127.0.0.1
```

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-17-port-scanner
```

Run the scanner:

```cmd
py port_scanner.py
```

To save the output:

```cmd
py port_scanner.py > output.txt
```

---

## 📊 Testing and Results

The scanner successfully executed against the local host:

```text
[*] Initiating Socket Sweep on: 127.0.0.1
--------------------------------------------------
[-] CLOSED: Port 22
[-] CLOSED: Port 80
[-] CLOSED: Port 443
[-] CLOSED: Port 5432
[-] CLOSED: Port 8080
```

The scan completed successfully and all five selected ports were identified as **CLOSED**.

---

## 📋 Result Summary

| Port   | Common Service | Result    |
| ------ | -------------- | --------- |
| `22`   | SSH            | 🔴 CLOSED |
| `80`   | HTTP           | 🔴 CLOSED |
| `443`  | HTTPS          | 🔴 CLOSED |
| `5432` | PostgreSQL     | 🔴 CLOSED |
| `8080` | Web / Proxy    | 🔴 CLOSED |

### Overall Result

```text
Target: 127.0.0.1

Ports Tested: 5
Open Ports: 0
Closed Ports: 5
```

---

## 🌐 Network Topology

```text
              Local Computer
                    │
                    ▼
               127.0.0.1
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
      22           80           443
      SSH         HTTP         HTTPS
    CLOSED       CLOSED       CLOSED
       │            │            │
       └────────────┼────────────┘
                    │
              ┌─────┴─────┐
              ▼           ▼
            5432         8080
         PostgreSQL   Web / Proxy
           CLOSED       CLOSED
```

---

## 🛡️ Security Analysis

The scan found no accessible services on the five selected ports during testing.

A **closed port does not automatically indicate a vulnerability**. It means that the scanner could not establish a TCP connection to a service on that port at the time of testing.

Regular port and service identification can help security teams understand the local attack surface and identify unexpectedly exposed services.

---

## 🔧 Recommendations

* Keep unnecessary services disabled.
* Review open ports regularly.
* Restrict services to required interfaces.
* Use appropriate firewall rules.
* Perform port assessments in authorized environments.
* Document unexpected services for further investigation.

---

## 📁 Project Structure

```text
Day-17-port-scanner/
│
├── port_scanner.py
├── output.png
|
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Localhost port scanning.
* TCP connection testing.
* Port status identification.
* Successful scanner execution.
* Saved scan output.
* Network topology mapping.

### Screenshot Caption

> **Figure 1: Localhost Port and Service Scanning Output**

---

## ✅ Conclusion

The Local Network Port and Service Scanning task was successfully completed in a controlled local environment.

The Python-based scanner tested ports **22, 80, 443, 5432, and 8080** on `127.0.0.1`. All five tested ports were reported as **CLOSED**.

The task provided practical understanding of basic TCP socket connections, port status identification, local service visibility, and network mapping.

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
