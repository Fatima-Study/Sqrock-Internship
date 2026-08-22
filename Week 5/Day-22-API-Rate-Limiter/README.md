# 🛡️ SQROCK IT SOLUTION — CYBERSECURITY INTERNSHIP

# 🚦 Day 22 — API Rate Limiting Token Bucket Logic

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Rate Limiting](https://img.shields.io/badge/Focus-API%20Rate%20Limiting-red)
![Token Bucket](https://img.shields.io/badge/Algorithm-Token%20Bucket-orange)
![Defensive Coding](https://img.shields.io/badge/Approach-Defensive%20Coding-purple)
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
- [Rate Limiting Logic](#-rate-limiting-logic)
- [Methodology](#️-methodology)
- [Implementation](#-implementation)
- [Testing and Results](#-testing-and-results)
- [Architecture](#-architecture)
- [Security Benefits](#-security-benefits)
- [Result Summary](#-result-summary)
- [Project Structure](#-project-structure)
- [Evidence](#-evidence)
- [Conclusion](#-conclusion)
- [Author & Contact](#author-contact)

---

## 📌 Overview

This project implements a Python-based **API Rate Limiter using Token Bucket Logic**.

The rate limiter maintains a token allocation for each client and controls whether incoming requests should be allowed or denied.

The implementation uses:

- Token capacity.
- Token refill rate.
- Client tracking.
- Request validation.
- Automatic token replenishment.

The system was tested using the local client:

```text
127.0.0.1
```

> ⚠️ **Safety Notice:** This project is intended for authorized local or isolated lab environments only.

---

## 🎯 Objective

The main objectives of this task are:

* Implement Token Bucket rate limiting logic.
* Maintain a token state for each client.
* Allow requests when tokens are available.
* Deny requests when the token allocation is exhausted.
* Refill tokens according to a defined rate.
* Verify automated request denial.
* Demonstrate the behavior through an execution loop.
* Understand the role of rate limiting in protecting application availability.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Python `time` Module**
* **Token Bucket Algorithm**
* **Stateful Request Tracking**
* **Command Prompt**
* **Local Security Lab**

---

## 🔍 Rate Limiting Logic

The implementation uses the **Token Bucket** mechanism.

The configured values are:

| Parameter      | Value          |
| -------------- | -------------- |
| Token Capacity | 3              |
| Refill Rate    | 0.5 tokens/sec |
| Client         | `127.0.0.1`    |

Initially, the client receives 3 tokens.

```text
Token Bucket

🪙  🪙  🪙
 3 Tokens
```

Each allowed request consumes one token.

```text
Request 1 → ALLOWED
Request 2 → ALLOWED
Request 3 → ALLOWED
```

After the available tokens are consumed, additional requests are denied until tokens are replenished.

```text
Request 4 → DENIED
Request 5 → DENIED
```

After waiting for token replenishment, another request can be allowed.

```text
After Refill → REQUEST ALLOWED
```

---

## ⚙️ Methodology

```text
Client Request
      ↓
Rate Limiter
      ↓
Check Client Token State
      ↓
Calculate Token Refill
      ↓
Check Available Token
      ↓
 ┌───────────────┐
 │ Token Available│
 └───────┬───────┘
         ↓
      ALLOW
         │
         ↓
Application

If Token Unavailable
         ↓
       DENY
         ↓
Rate Limit Response
```

---

## 💻 Implementation

The rate limiter is implemented using a Python class.

### RateLimiter Class

```python
class RateLimiter:

    def __init__(self, token_capacity, refill_rate_per_sec):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}
```

The class stores:

* Maximum token capacity.
* Token refill rate.
* Client-specific token information.

### Request Validation

The `allow_request()` function checks the client's token state.

```python
if state["tokens"] >= 1:
    state["tokens"] -= 1
    return True

return False
```

If a token is available, the request is allowed.

If no token is available, the request is denied.

### Token Refill

Tokens are replenished according to elapsed time:

```python
elapsed = now - state["last_updated"]

state["tokens"] = min(
    self.capacity,
    state["tokens"] + (elapsed * self.refill_rate)
)
```

This allows the token bucket to gradually recover after requests have consumed available tokens.

---

## 📊 Testing and Results

The rate limiter was tested using seven consecutive requests followed by a token refill verification.

### Test Results

| Test         | Result    | Observation         |
| ------------ | --------- | ------------------- |
| Request 1    | ✅ ALLOWED | Token available     |
| Request 2    | ✅ ALLOWED | Token available     |
| Request 3    | ✅ ALLOWED | Token available     |
| Request 4    | ❌ DENIED  | Rate limit reached  |
| Request 5    | ❌ DENIED  | No sufficient token |
| Request 6    | ❌ DENIED  | No sufficient token |
| Request 7    | ❌ DENIED  | No sufficient token |
| After Refill | ✅ ALLOWED | Token replenished   |

The execution successfully demonstrated both **request denial** and **token refill behavior**.

---

## 🏗️ Architecture

The Token Bucket rate limiter can be represented using the following architecture:

```text
        Client
          │
          ↓
     API Gateway
          │
          ↓
    Rate Limiter
          │
          ↓
     Token Bucket
          │
          ↓
    Check Token State
       ┌──┴──┐
       │     │
       ↓     ↓
    ALLOW   DENY
       │     │
       ↓     ↓
 Application  Rate Limit
              Response
```

### Architecture Flow

1. A client sends a request.
2. The request reaches the rate limiter.
3. The client's token state is checked.
4. If a token is available, the request is allowed.
5. If no token is available, the request is denied.
6. Tokens are gradually replenished according to the configured refill rate.

---

## 🛡️ Security Benefits

Rate limiting can help protect application services against:

* Excessive automated requests.
* Rapid credential testing.
* Resource exhaustion.
* Uncontrolled API access.
* Certain Denial-of-Service conditions.

A properly configured rate limiter helps maintain application availability by controlling request volume.

---

## 📋 Result Summary

```text
Rate Limiter Implementation   → PASS
Token Bucket Logic            → PASS
Client Tracking               → PASS
Allowed Requests              → PASS
Request Denial                → PASS
Token Refill                  → PASS
Execution Loop Verification   → PASS
```

### Overall Findings

| Security Check       | Result       |
| -------------------- | ------------ |
| Token Capacity       | ✅ Configured |
| Request Allow Logic  | ✅ Working    |
| Request Denial Logic | ✅ Working    |
| Rate Limit Trigger   | ✅ Verified   |
| Token Refill         | ✅ Verified   |
| Local Execution      | ✅ Successful |

---

## 📁 Project Structure

```text
Day-22-API-Rate-Limiter/
│
├── rate_limiter.py
├── output.png
│
└── README.md
```

---

## 📸 Evidence

The project includes evidence of:

* Token Bucket implementation.
* Token capacity configuration.
* Client request tracking.
* Allowed request results.
* Rate limit denial results.
* Token refill verification.
* Successful Python execution.

---

## ✅ Conclusion

The **API Rate Limiting Token Bucket Logic** was successfully implemented and tested in a controlled local environment.

The system successfully allowed requests while tokens were available, denied requests after the token allocation was exhausted, and allowed another request after token replenishment.

This task provided practical experience with **stateful request tracking, Token Bucket rate limiting, automated request denial, and defensive API security concepts**.

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
