print("🐍 PYTHON QUIZ CHALLENGE 🐍")
print("=" * 35)

questions = (
    "Which keyword is used to define a function?",
    "Which data type stores True or False?",
    "What is the output of 2 ** 3?",
    "Which symbol is used for comments?",
    "Which method adds an item to a list?"
)

options = (
    ("A. func", "B. def", "C. function", "D. define"),
    ("A. int", "B. float", "C. bool", "D. str"),
    ("A. 6", "B. 8", "C. 9", "D. 5"),
    ("A. //", "B. #", "C. --", "D. /*"),
    ("A. add()", "B. insert()", "C. append()", "D. push()")
)

answers = ("B", "C", "B", "B", "C")

score = 0

for i in range(len(questions)):

    print("\n" + questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("👉 Your answer: ").upper()

    if user_answer == answers[i]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", answers[i])

# Result
total = len(questions)
percentage = (score / total) * 100

print("\n" + "=" * 35)
print("🏆 QUIZ COMPLETED!")
print("=" * 35)

print(f"Score: {score}/{total}")
print(f"Percentage: {percentage}%")

if percentage == 100:
    print("🔥 Perfect! Python Master!")
elif percentage >= 80:
    print("🚀 Excellent!")
elif percentage >= 60:
    print("👍 Good job!")
elif percentage >= 40:
    print("📚 Keep practicing!")
else:
    print("💪 Keep learning!")