# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🛡️ Day 24 — Automated Threat Intelligence IP Blocking Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Threat Intelligence](https://img.shields.io/badge/Focus-Threat%20Intelligence-red)
![IP Blocking](https://img.shields.io/badge/Function-IP%20Blocking-orange)
![Security Automation](https://img.shields.io/badge/Approach-Security%20Automation-purple)
![Local Lab](https://img.shields.io/badge/Environment-Local%20Lab-blueviolet)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

<p align="center">
  <b>SQROCK IT SOLUTION — Alpha 2 Cybersecurity Internship</b>
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Objective](#-objective)
- [Technologies Used](#️-technologies-used)
- [Threat Intelligence Checks](#-threat-intelligence-checks)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Execution](#️-execution)
- [Testing and Results](#-testing-and-results)
- [Security Findings](#-security-findings)
- [Architecture](#-architecture)
- [Security Benefits](#-security-benefits)
- [Result Summary](#-result-summary)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **Automated Threat Intelligence IP Blocking Pipeline**.

The system processes a mock Threat Intelligence feed containing IP addresses, indicators, and risk scores.

Each indicator is evaluated against a defined risk threshold:

- Risk score greater than `90` → High-risk IP → Simulated block rule.
- Risk score `90` or below → Suspicious activity → Logged for monitoring.

The implementation demonstrates how threat intelligence data can be processed and used to support automated defensive security decisions.

> ⚠️ **Safety Notice:** This project uses a controlled mock threat-intelligence feed and simulated firewall actions for authorized local lab testing only.

---

## 🎯 Objective

The main objectives of this task are:

- Ingest a mock Threat Intelligence feed.
- Parse IP addresses and threat indicators.
- Evaluate risk scores.
- Identify high-risk IP addresses.
- Simulate deployment of block rules for high-risk indicators.
- Log suspicious activity below the blocking threshold.
- Verify automated defensive decision-making.
- Understand the role of Threat Intelligence in security automation.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **JSON Data Structures**
- **Threat Intelligence Indicators**
- **Risk Score Evaluation**
- **Security Automation**
- **Command Prompt**
- **Local Security Lab**

---

## 🔍 Threat Intelligence Checks

The pipeline performs the following checks:

| IP Address | Indicator | Risk Score | Action |
|---|---|---:|---|
| `103.45.67.89` | `malware_c2` | 98 | 🔴 BLOCK |
| `185.10.11.12` | `botnet_node` | 85 | 🟡 LOG |
| `198.51.100.33` | `brute_forcer` | 92 | 🔴 BLOCK |

### Risk Threshold

```text
Risk Score > 90
        ↓
HIGH RISK
        ↓
Simulated Block Rule
```

```text
Risk Score ≤ 90
        ↓
Suspicious Activity
        ↓
Log for Monitoring
```

---

## ⚙️ Methodology

```text
Threat Intelligence Feed
          ↓
      Feed Ingestion
          ↓
   Parse IP + Indicator
          ↓
    Evaluate Risk Score
          ↓
     Check Threshold
          ↓
 ┌────────────────────┐
 │ Risk Score > 90 ?  │
 └─────────┬──────────┘
           ↓
      ┌────┴────┐
      ↓         ↓
    BLOCK      LOG
      ↓         ↓
High-Risk    Suspicious
 Indicator    Activity
      ↓         ↓
Simulated    Monitoring
Firewall
Rule
```

---

## 💻 Implementation

The project uses a mock Threat Intelligence feed containing IP addresses, indicators, and risk scores.

### Mock Threat Intelligence Feed

```python
MOCK_INTEL_FEED = [
    {
        "ip": "103.45.67.89",
        "indicator": "malware_c2",
        "risk_score": 98
    },
    {
        "ip": "185.10.11.12",
        "indicator": "botnet_node",
        "risk_score": 85
    },
    {
        "ip": "198.51.100.33",
        "indicator": "brute_forcer",
        "risk_score": 92
    }
]
```

### Risk Evaluation

The pipeline evaluates each threat-intelligence entry.

```python
if risk_score > 90:

    print(
        f"[ACTION] HIGH RISK - Deploying block rule for IP: "
        f"{ip} (Reason: {indicator}, Risk Score: {risk_score})"
    )
```

When the risk score is above `90`, the system generates a simulated blocking action.

For lower-risk indicators, the activity is logged:

```python
else:

    print(
        f"[*] LOGGING - Suspicious activity monitored for IP: "
        f"{ip} (Reason: {indicator}, Risk Score: {risk_score})"
    )
```

---

## ▶️ Execution

Navigate to the project directory:

```cmd
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-24-Threat-Intel-IP-Blocking
```

Run the pipeline:

```cmd
python threat_intel_blocker.py
```

To save the execution output:

```cmd
python threat_intel_blocker.py > output.txt
```

To view the saved output:

```cmd
type output.txt
```

---

## 📊 Testing and Results

The Threat Intelligence pipeline was successfully executed using the mock feed.

### Expected Execution Result

```text
[*] Ingesting Threat Intelligence Feed...
------------------------------------------------------------
[ACTION] HIGH RISK - Deploying block rule for IP: 103.45.67.89 (Reason: malware_c2, Risk Score: 98)
[*] LOGGING - Suspicious activity monitored for IP: 185.10.11.12 (Reason: botnet_node, Risk Score: 85)
[ACTION] HIGH RISK - Deploying block rule for IP: 198.51.100.33 (Reason: brute_forcer, Risk Score: 92)
```

### Test Results

| Test                      | Result   | Observation                 |
| ------------------------- | -------- | --------------------------- |
| Threat Feed Ingestion     | ✅ PASS   | Feed successfully processed |
| IP `103.45.67.89`         | 🔴 BLOCK | Risk score 98               |
| IP `185.10.11.12`         | 🟡 LOG   | Risk score 85               |
| IP `198.51.100.33`        | 🔴 BLOCK | Risk score 92               |
| Risk Threshold Evaluation | ✅ PASS   | Threshold logic worked      |
| Automated Decision        | ✅ PASS   | Block/Log action generated  |

---

## 🚨 Security Findings

### Finding 1 — High-Risk Malware C2 Indicator

```text
IP: 103.45.67.89
Indicator: malware_c2
Risk Score: 98
```

The risk score is greater than `90`.

Therefore, the pipeline generates:

```text
[ACTION] HIGH RISK - Deploying block rule
```

---

### Finding 2 — Suspicious Botnet Indicator

```text
IP: 185.10.11.12
Indicator: botnet_node
Risk Score: 85
```

The risk score is below the blocking threshold.

The pipeline therefore records the activity for monitoring:

```text
[*] LOGGING - Suspicious activity monitored
```

---

### Finding 3 — High-Risk Brute-Force Indicator

```text
IP: 198.51.100.33
Indicator: brute_forcer
Risk Score: 92
```

The risk score exceeds the threshold.

The pipeline generates a simulated blocking action.

---

## 🏗️ Architecture

The automated Threat Intelligence pipeline follows this architecture:

```text
          Threat Intelligence Feed
                    │
                    ↓
             Feed Ingestion
                    │
                    ↓
             Indicator Parser
                    │
                    ↓
              Risk Scoring
                    │
                    ↓
           Threshold Evaluation
                    │
              ┌─────┴─────┐
              ↓           ↓
        Risk Score >90   ≤ 90
              ↓           ↓
          HIGH RISK     LOG
              ↓           ↓
      Simulated Block   Monitor
          Rule
```

### Operational Flow

1. Threat Intelligence data is received.
2. IP address and indicator information is parsed.
3. The risk score is evaluated.
4. High-risk indicators trigger a simulated block action.
5. Lower-risk suspicious indicators are logged.
6. The results are recorded for security review.

---

## 🛡️ Security Benefits

Threat Intelligence automation can help security teams:

* Identify high-risk indicators quickly.
* Automate defensive decisions.
* Reduce manual response time.
* Maintain logs of suspicious activity.
* Integrate threat intelligence into security workflows.
* Support proactive network defense.

The pipeline demonstrates a simplified defensive workflow where threat intelligence can drive automated security actions.

---

## 📋 Result Summary

```text
Threat Feed Ingestion       → PASS
Indicator Parsing           → PASS
Risk Score Evaluation       → PASS
High-Risk Detection         → PASS
Simulated Block Generation  → PASS
Suspicious Activity Logging → PASS
Execution Verification      → PASS
```

### Overall Findings

| Security Check           | Result          |
| ------------------------ | --------------- |
| Threat Intelligence Feed | ✅ Processed     |
| Risk Score `98`          | 🔴 Block Action |
| Risk Score `85`          | 🟡 Logged       |
| Risk Score `92`          | 🔴 Block Action |
| Automated Decision Logic | ✅ Successful    |
| Local Lab Execution      | ✅ Successful    |

---

## 📁 Project Structure

```text
Day-24-Threat-Intel-IP-Blocking/
│
├── threat_intel_blocker.py
├── output.png
│
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Threat Intelligence feed ingestion.
* IP indicator processing.
* Risk score evaluation.
* High-risk IP detection.
* Simulated firewall block actions.
* Suspicious activity logging.
* Successful pipeline execution.
* Operational architecture.

---

## ✅ Conclusion

The **Automated Threat Intelligence IP Blocking Pipeline** was successfully implemented using Python in a controlled local laboratory environment.

The pipeline successfully processed the mock Threat Intelligence feed, evaluated risk scores, generated simulated block actions for high-risk indicators, and logged suspicious activity below the defined threshold.

This task provided practical experience with **Threat Intelligence ingestion, risk-based decision-making, security automation, indicator processing, defensive IP blocking concepts, and operational security workflows**.

---

<a name="author-contact"></a>

## 👩‍💻 Author & Contact

<p align="center">
  <img src="https://github.com/Fatima-Study.png" width="120" alt="Fatima">
</p>

<p align="center">
  <strong>Fatima</strong><br>
  Cybersecurity | SQROCK IT SOLUTION - Internship (Aug-Sep 2026 Batch)
</p>

<p align="center">
  <a href="https://github.com/Fatima-Study">
    GitHub
  </a>
  |
  <a href="https://linkedin.com/in/fatima-taufique-1313b633b">
    LinkedIn
  </a>
</p>
