from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd


# 50 sample emails
emails = [
    # Phishing emails
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Urgent update your bank details to avoid closure",
    "Your account has been locked verify now",
    "Confirm your password immediately",
    "You have won a cash prize click the link",
    "Urgent security alert verify your login",
    "Your payment failed update your card details",
    "Click now to secure your account",
    "Your mailbox will be disabled verify immediately",
    "Confirm your identity using this link",
    "Urgent action required update your account",
    "Your bank account needs verification",
    "Click the link to prevent account closure",
    "Your password has expired reset it now",
    "Security warning verify your credentials",
    "Claim your reward by clicking this link",
    "Your account will be suspended today",
    "Update your payment information immediately",
    "Verify your PayPal login now",
    "Urgent invoice payment required click here",
    "Your account has suspicious activity verify now",
    "Confirm your banking information immediately",
    "Click here to restore your account",
    "Your email account requires urgent verification",

    # Legitimate emails
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Meeting notes from yesterday are attached",
    "The project meeting is scheduled for Monday",
    "Please review the quarterly report",
    "Your training session starts at 10am",
    "The office will be closed on Friday",
    "Here is the presentation from today's meeting",
    "Please submit your weekly report",
    "The team meeting has been moved to Tuesday",
    "Your vacation request has been approved",
    "Please review the project timeline",
    "The monthly newsletter is attached",
    "Your appointment is scheduled for tomorrow",
    "The development team completed the task",
    "Please attend the security awareness session",
    "The report is ready for discussion",
    "Your employee training certificate is available",
    "The meeting room has been reserved",
    "Please check the attached project document",
    "The team lunch is scheduled for Friday",
    "Your application has been received",
    "Please review the updated policy document",
    "The project deadline is next week",
    "Thank you for attending the meeting"
]

# 1 = phishing, 0 = legitimate
labels = [1] * 25 + [0] * 25


# Create dataset
data = pd.DataFrame({
    "email": emails,
    "label": labels
})


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    data["email"],
    data["label"],
    test_size=0.2,
    random_state=42,
    stratify=data["label"]
)


# Build ML pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])


# Train model
model.fit(X_train, y_train)


# Test model
predictions = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("=" * 60)
print("       PHISHING EMAIL DETECTION USING ML")
print("=" * 60)

print(f"\nDataset Size : {len(data)} emails")
print(f"Training Data: {len(X_train)} emails")
print(f"Testing Data : {len(X_test)} emails")

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Confusion matrix
matrix = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(matrix)


# Test new emails
test_emails = [
    "Please verify your PayPal login immediately",
    "Meeting notes from yesterday",
    "Urgent update your bank account now",
    "The team meeting is scheduled for tomorrow"
]

print("\nNew Email Predictions:")
print("-" * 60)

for email in test_emails:
    prediction = model.predict([email])[0]

    result = "PHISHING" if prediction == 1 else "LEGIT"

    print(f"{result}: {email}")


print("\nDetection completed successfully!")
