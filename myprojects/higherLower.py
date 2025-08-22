
#--------
# THE HIGHER LOWER GAME
#-------

import random

score = 0

# List of questions as dictionaries
questions = [
    {
        "question": "Which one of the following celebrities has the highest net worth?",
        "options": {"A": "RONALDO", "B": "Virat Kohli"},
        "correct": "A"
    },
    {
        "question": "Which company is older?",
        "options": {"A": "Microsoft", "B": "Google"},
        "correct": "A"
    },
    {
        "question": "Which country has the larger population?",
        "options": {"A": "India", "B": "USA"},
        "correct": "A"
    },
    {
        "question": "Which planet is closer to the Sun?",
        "options": {"A": "Venus", "B": "Mars"},
        "correct": "A"
    },
    {
        "question": "Who has won more Grand Slam titles?",
        "options": {"A": "Roger Federer", "B": "Rafael Nadal"},
        "correct": "B"
    }
]

def high_low(score):
    print("Welcome to the Higher Lower Game!")
    while True:
        # Pick a random question
        q = random.choice(questions)

        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"{key}: {value}")

        answer = input("Enter your answer (A or B): ").strip().upper()

        if answer != q["correct"]:
            print("❌ You lose!\nGame over.")
            break
        else:
            print("✅ You won!")
            score += 1
            print(f"🎯 Your current score is {score}")
            return score  # Return updated score

while True:
    score = high_low(score)  # Update the score
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋 Goodbye!")
        break
