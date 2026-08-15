import json


QUESTIONS = [
    {
        "q": "An email asks you to verify your password through a link. What should you do?",
        "opts": [
            "A) Click the link",
            "B) Contact IT through an official channel",
            "C) Reply with your password"
        ],
        "ans": "B",
        "exp": "Always verify suspicious requests through official channels."
    },

    {
        "q": "You find an unknown USB drive in a parking lot. What should you do?",
        "opts": [
            "A) Plug it into your computer",
            "B) Give it to security or IT",
            "C) Open the files on another computer"
        ],
        "ans": "B",
        "exp": "Unknown USB devices can be used for baiting attacks."
    },

    {
        "q": "A caller claims to be from IT and asks for your password. What should you do?",
        "opts": [
            "A) Provide the password",
            "B) Ask for their personal number",
            "C) Refuse and verify through official IT channels"
        ],
        "ans": "C",
        "exp": "Legitimate IT staff should not request your password."
    },

    {
        "q": "Which is a common phishing warning sign?",
        "opts": [
            "A) Urgent request for sensitive information",
            "B) Normal internal announcement",
            "C) Expected meeting reminder"
        ],
        "ans": "A",
        "exp": "Urgency is commonly used to pressure users into making mistakes."
    },

    {
        "q": "What does MFA provide?",
        "opts": [
            "A) An additional authentication factor",
            "B) Free internet access",
            "C) Automatic antivirus protection"
        ],
        "ans": "A",
        "exp": "MFA adds another verification factor during authentication."
    },

    {
        "q": "What should you do before clicking an unexpected link?",
        "opts": [
            "A) Click it immediately",
            "B) Verify the sender and destination",
            "C) Forward it to everyone"
        ],
        "ans": "B",
        "exp": "Unexpected links should be verified before opening."
    },

    {
        "q": "What is social engineering?",
        "opts": [
            "A) Manipulating people to obtain information or perform actions",
            "B) Installing a printer",
            "C) Designing a website"
        ],
        "ans": "A",
        "exp": "Social engineering targets human behavior rather than only technical systems."
    },

    {
        "q": "A suspicious message asks you to keep a request secret. What is the safest action?",
        "opts": [
            "A) Follow the instructions",
            "B) Verify the request independently",
            "C) Delete your security software"
        ],
        "ans": "B",
        "exp": "Secrecy and pressure can be social-engineering warning signs."
    },

    {
        "q": "What is smishing?",
        "opts": [
            "A) SMS-based phishing",
            "B) Physical security testing",
            "C) Password encryption"
        ],
        "ans": "A",
        "exp": "Smishing is phishing conducted through SMS or text messages."
    },

    {
        "q": "What is vishing?",
        "opts": [
            "A) Voice phishing",
            "B) Video encryption",
            "C) Virus scanning"
        ],
        "ans": "A",
        "exp": "Vishing is social engineering conducted through voice calls."
    },

    {
        "q": "Which action is safest when receiving an unexpected attachment?",
        "opts": [
            "A) Open it immediately",
            "B) Verify the sender and attachment first",
            "C) Disable antivirus software"
        ],
        "ans": "B",
        "exp": "Unexpected attachments should be verified before opening."
    },

    {
        "q": "What is a good response to a suspicious account-reset request?",
        "opts": [
            "A) Use the link in the message",
            "B) Contact the organization through its official website or number",
            "C) Share your login details"
        ],
        "ans": "B",
        "exp": "Use trusted official channels instead of links or contact details in suspicious messages."
    }
]


def run_quiz():
    score = 0
    results = []

    print("=" * 60)
    print("     SOCIAL ENGINEERING AWARENESS QUIZ")
    print("=" * 60)

    for i, q in enumerate(QUESTIONS, 1):

        print(f"\nQ{i}: {q['q']}")

        for option in q["opts"]:
            print(option)

        answer = input("Your answer (A/B/C): ").strip().upper()

        if answer == q["ans"]:
            print("✓ Correct!")
            score += 1
            result = "Correct"
        else:
            print("✗ Incorrect.")
            print("Explanation:", q["exp"])
            result = "Incorrect"

        results.append({
            "question": q["q"],
            "your_answer": answer,
            "correct_answer": q["ans"],
            "result": result
        })

    percentage = (score / len(QUESTIONS)) * 100

    print("\n" + "=" * 60)
    print("QUIZ COMPLETED")
    print("=" * 60)
    print(f"Score: {score}/{len(QUESTIONS)}")
    print(f"Percentage: {percentage:.2f}%")

    report = {
        "total_questions": len(QUESTIONS),
        "correct_answers": score,
        "percentage": percentage,
        "results": results
    }

    with open("score_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nScore report saved as: score_report.json")


if __name__ == "__main__":
    run_quiz()
