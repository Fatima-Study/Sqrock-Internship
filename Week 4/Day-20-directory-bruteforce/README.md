# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

## 🔎 Day 20 — Web Directory Brute-Force Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Web Security](https://img.shields.io/badge/Focus-Web%20Security-red)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-orange)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

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
- [Target and Wordlist](#-target-and-wordlist)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Detection Summary](#-detection-summary)
- [Security Analysis](#️-security-analysis)
- [Defensive Recommendations](#-defensive-recommendations)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **Web Directory Brute-Force Simulation** for authorized local security testing.

The script checks a predefined list of common web paths against a local web server and analyzes the returned HTTP status codes.

The purpose is to identify whether potentially sensitive or administrative routes are accessible.

> ⚠️ **Safety Notice:** This project was performed against a controlled local environment (`localhost`) for educational and defensive security testing only.

---

## 🎯 Objective

The main objectives of this task are:

- Simulate targeted web directory discovery.
- Test predefined endpoint paths.
- Analyze HTTP response status codes.
- Identify accessible routes.
- Identify restricted routes.
- Detect unavailable routes.
- Understand the security risks associated with exposed web resources.
- Develop defensive recommendations for secure web deployments.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Requests Library**
- **HTTP**
- **Local Web Server**
- **Command Prompt**
- **Predefined Wordlist**

---

## 🎯 Target and Wordlist

### Target

```text
http://localhost:5000
```

The target is a locally hosted web server used for authorized testing.

### Wordlist

The following paths were tested:

```text
admin
dashboard
api/v1
.env
backup.sql
```

These paths represent examples of administrative areas, application routes, configuration files, and backup resources that should not be unnecessarily exposed.

---

## ⚙️ Methodology

```text
Local Web Server
       ↓
Define Target URL
       ↓
Load Predefined Wordlist
       ↓
Build Endpoint URL
       ↓
Send HTTP Request
       ↓
Check HTTP Status Code
       ↓
Classify Result
       ↓
Generate Detection Log
       ↓
Save Output
```

---

## 💻 Implementation

The Python scanner uses the `requests` library to send HTTP GET requests to each predefined path.

For each endpoint, the scanner checks the HTTP response:

| HTTP Status  | Scanner Result                    |
| ------------ | --------------------------------- |
| `200`        | 🟢 Route Accessible               |
| `403`        | 🟠 Restricted Route               |
| Other status | ⚪ Not Accessible / Other Response |

The scanner also uses a request timeout to prevent the process from waiting indefinitely for an unavailable endpoint.

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-20-directory-scanner
```

Start the local HTTP server:

```cmd
py -m http.server 5000
```

Keep the server running.

Open a second Command Prompt and navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-20-directory-scanner
```

Run the scanner:

```cmd
py directory_scanner.py
```

To save the result:

```cmd
py directory_scanner.py > output.txt
```

To view the saved output:

```cmd
type output.txt
```

---

## 📊 Testing and Results

The scanner successfully tested all five predefined endpoints against the local server.

### Actual Output

```text
[*] Discovering endpoints for: http://localhost:5000
------------------------------------------------------------
[-] Not Accessible: http://localhost:5000/admin (Status: 404)
[-] Not Accessible: http://localhost:5000/dashboard (Status: 404)
[-] Not Accessible: http://localhost:5000/api/v1 (Status: 404)
[-] Not Accessible: http://localhost:5000/.env (Status: 404)
[-] Not Accessible: http://localhost:5000/backup.sql (Status: 404)
```

---

## 📋 Detection Summary

| Endpoint      | HTTP Status | Result      |
| ------------- | ----------: | ----------- |
| `/admin`      |       `404` | ⚪ Not Found |
| `/dashboard`  |       `404` | ⚪ Not Found |
| `/api/v1`     |       `404` | ⚪ Not Found |
| `/.env`       |       `404` | ⚪ Not Found |
| `/backup.sql` |       `404` | ⚪ Not Found |

### Overall Result

```text
Total Endpoints Tested : 5
Accessible Routes      : 0
Restricted Routes      : 0
Not Found Routes       : 5
```

---

## 🔐 Security Analysis

The scanner did not find any of the tested paths as accessible on the local server.

A `404 Not Found` response indicates that the requested resource was not available at the tested URL.

### Tested Resources

#### `/admin`

Administrative areas should be protected with appropriate authentication and authorization controls.

#### `/dashboard`

Application dashboards should not be publicly accessible without proper access control.

#### `/api/v1`

API routes should expose only intended functionality and should use appropriate authentication and authorization mechanisms.

#### `/.env`

Environment files can contain sensitive configuration information and should never be exposed through the web server.

#### `/backup.sql`

Database backups may contain sensitive information and should be stored outside publicly accessible web directories.

> A `404` result in this local test confirms that the tested resource was not found at that path. It does not by itself prove that a complete production deployment is secure.

---

## 🛡️ Defensive Recommendations

### 1. Restrict Sensitive Files

Files such as:

```text
.env
backup.sql
```

should be stored outside publicly accessible web directories.

### 2. Protect Administrative Routes

Routes such as:

```text
/admin
/dashboard
```

should require strong authentication and authorization.

### 3. Use Custom Routing Controls

Applications should explicitly define which routes are available instead of unintentionally exposing filesystem resources.

### 4. Disable Unnecessary Directory Exposure

Web servers should not expose unnecessary directories or sensitive files.

### 5. Apply Access Control

Sensitive application resources should be protected using appropriate access-control policies.

### 6. Monitor HTTP Requests

Repeated requests for sensitive paths can be logged and investigated as potential reconnaissance activity.

---

## 🧪 Testing Checklist

| Test                  | Result |
| --------------------- | ------ |
| Local server started  | ✅ PASS |
| Target reachable      | ✅ PASS |
| `/admin` checked      | ✅ PASS |
| `/dashboard` checked  | ✅ PASS |
| `/api/v1` checked     | ✅ PASS |
| `/.env` checked       | ✅ PASS |
| `/backup.sql` checked | ✅ PASS |
| HTTP status detected  | ✅ PASS |
| Output generated      | ✅ PASS |

---

## 📁 Project Structure

```text
Day-20-directory-scanner/
│
├── directory_scanner.py
├── output.png
|
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Local web server execution.
* Authorized localhost endpoint testing.
* Predefined wordlist scanning.
* HTTP status code analysis.
* Endpoint discovery results.
* `404 Not Found` responses.
* Saved scanner output.

---

## ✅ Conclusion

The **Web Directory Brute-Force Simulation** was successfully implemented and tested against a controlled local web server.

A total of **5 predefined endpoints** were tested:

```text
/admin
/dashboard
/api/v1
/.env
/backup.sql
```

All five tested endpoints returned:

```text
HTTP 404 — Not Found
```

Therefore, none of the tested resources were accessible through the local server at the time of testing.

This task demonstrated how automated HTTP requests and response-code analysis can be used for basic web endpoint discovery and defensive security assessment.

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
```
