# 🛡️ SQROCK IT SOLUTION — Cybersecurity Internship

# 🎯 Day 12 — Phishing Email Detection with Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Naive%20Bayes-orange)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Dataset](https://img.shields.io/badge/Dataset-50%20Samples-purple)
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
- [🧠 Key Concepts](#key-concepts)
- [📊 Dataset](#dataset)
- [🛠️ Tools & Technologies](#tools--technologies)
- [🔍 Methodology](#methodology)
- [⚙️ Features](#features)
- [📂 Project Structure](#project-structure)
- [🚀 How to Run](#how-to-run)
- [📈 Model Evaluation](#model-evaluation)
- [📊 Confusion Matrix](#confusion-matrix)
- [📄 Accuracy Report](#accuracy-report)
- [🛡️ Security Awareness](#security-awareness)
- [🔐 Ethical & Legal Notice](#ethical--legal-notice)
- [📚 Learning Outcomes](#learning-outcomes)
- [📈 Conclusion](#conclusion)
- [👩‍💻 Author & Contact](#author-contact)

---

<a name="overview"></a>

## 📌 Overview

Day 12 focuses on **Phishing Email Detection using Machine Learning**.

The project implements a **Multinomial Naive Bayes classifier** to classify emails as either **Phishing** or **Legitimate**.

A 50-sample dataset is used for training and evaluation. Text features are extracted using `CountVectorizer`, and the model performance is evaluated using accuracy and a confusion matrix.

---

<a name="objective"></a>

## 🎯 Objective

The objective of this task is to develop a machine-learning-based phishing email detector that can identify suspicious email messages and distinguish them from legitimate messages.

The project demonstrates the use of text classification techniques for cybersecurity applications.

---

<a name="key-concepts"></a>

## 🧠 Key Concepts

The project covers:

- Phishing Email Detection
- Machine Learning
- Text Classification
- Multinomial Naive Bayes
- CountVectorizer
- Training and Testing Data
- Accuracy
- Confusion Matrix
- Email Classification

---

<a name="dataset"></a>

## 📊 Dataset

The project uses a **50-sample email dataset** consisting of:

- **25 Phishing Emails**
- **25 Legitimate Emails**

Each email is assigned a label:

```text
1 → Phishing
0 → Legitimate
```
The dataset contains examples of common phishing indicators such as:

* Urgent requests
* Account verification
* Password requests
* Banking-related requests
* Suspicious links
* Prize or reward claims

Legitimate samples include normal workplace and communication-related emails.

---

<a name="tools--technologies"></a>

## 🛠️ Tools & Technologies

* **Python 3.x**
* **Pandas**
* **Scikit-learn**
* **CountVectorizer**
* **Multinomial Naive Bayes**
* **Command Prompt**
* **GitHub**

---

<a name="methodology"></a>

## 🔍 Methodology

```text
Collect 50 Email Samples
          ↓
Label Emails
          ↓
Phishing / Legitimate
          ↓
Split Dataset
          ↓
Convert Text into Features
          ↓
CountVectorizer
          ↓
Train Naive Bayes Model
          ↓
Test Model
          ↓
Calculate Accuracy
          ↓
Generate Confusion Matrix
          ↓
Classify New Emails
```

---

<a name="features"></a>

## ⚙️ Features

* 50-sample email dataset
* Phishing and legitimate email classification
* Text feature extraction
* Multinomial Naive Bayes classifier
* Train-test split
* Accuracy calculation
* Confusion matrix generation
* New email prediction
* Text-based output
* Local execution

---

<a name="project-structure"></a>

## 📂 Project Structure

```text
Day-12-Phishing-ML/
│
├── phishing_email_detector.py
├── email_detect_output.png
│
└── README.md
```

---

<a name="how-to-run"></a>

## 🚀 How to Run

### 1. Install Required Libraries

Open Command Prompt and run:

```bash
py -m pip install scikit-learn pandas
```

### 2. Navigate to the Project Folder

```bash
cd C:\Users\AA\Desktop\Sqrock_Cybersecurity_Internship\Day-12-Phishing-ML
```

### 3. Run the Program

```bash
py phishing_email_detector.py
```

---

<a name="model-evaluation"></a>

## 📈 Model Evaluation

The model is evaluated using a test portion of the 50-sample dataset.

The program reports:

* Dataset size
* Training samples
* Testing samples
* Accuracy
* Confusion matrix
* Predictions for new emails

Example output:

```text
Dataset Size : 50 emails
Training Data: 40 emails
Testing Data : 10 emails

Accuracy: XX.XX%
```

> Replace `XX.XX%` with the actual accuracy obtained from your program.

---

<a name="confusion-matrix"></a>

## 📊 Confusion Matrix

The project generates a confusion matrix to evaluate classification performance.

```text
                Predicted
              Legit  Phishing

Actual Legit     TN      FP

Actual Phishing  FN      TP
```

Where:

* **TN — True Negative:** Legitimate email correctly classified.
* **FP — False Positive:** Legitimate email incorrectly classified as phishing.
* **FN — False Negative:** Phishing email incorrectly classified as legitimate.
* **TP — True Positive:** Phishing email correctly classified.

The actual confusion matrix generated by the program is included in the project output.

---

<a name="accuracy-report"></a>

## 📄 Accuracy Report

The project includes:

```text
accuracy_report.txt
```

The report records the model evaluation results.

Example:

```text
Day 12 — Phishing Email Detection with ML

Dataset Size: 50 emails
Training Samples: 40
Testing Samples: 10

Accuracy: [ACTUAL ACCURACY]%

Confusion Matrix:
[ACTUAL CONFUSION MATRIX]

Model:
Multinomial Naive Bayes

Feature Extraction:
CountVectorizer
```

The accuracy value should reflect the actual result produced by the program.

---

<a name="security-awareness"></a>

## 🛡️ Security Awareness

Machine-learning-based email classification can assist in identifying suspicious messages.

Common phishing indicators include:

* Urgent or threatening language
* Requests for passwords or credentials
* Unexpected account-verification requests
* Suspicious links
* Banking or payment-related requests
* Unusual requests for sensitive information

Users should verify suspicious requests through trusted and official channels.

---

<a name="ethical--legal-notice"></a>

## 🔐 Ethical & Legal Notice

This project is developed strictly for **authorized cybersecurity education, research, and laboratory testing**.

* No real phishing campaign was conducted.
* No real users were targeted.
* No real credentials were collected.
* The dataset contains sample email text for educational purposes.
* The model is intended for learning and demonstration.
* The project should not be used to conduct unauthorized phishing activities.

---

<a name="learning-outcomes"></a>

## 📚 Learning Outcomes

Through this task, I learned:

* Basics of machine learning for cybersecurity
* Phishing email classification
* Text feature extraction
* CountVectorizer
* Multinomial Naive Bayes
* Dataset splitting
* Model evaluation
* Accuracy calculation
* Confusion matrix analysis
* Automated email prediction

---

<a name="conclusion"></a>

## 📈 Conclusion

The Day 12 project successfully demonstrates a machine-learning-based approach to phishing email detection.

Using a 50-sample dataset, CountVectorizer, and a Multinomial Naive Bayes classifier, the project performs text classification and evaluates the model using accuracy and a confusion matrix.

This task provided practical experience in applying machine learning concepts to a real-world cybersecurity problem.

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
