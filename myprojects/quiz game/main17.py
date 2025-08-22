from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Start quiz
quiz = QuizBrain(question_bank)

# Keep asking questions
while quiz.still_has_question():
    quiz.next_question()

# End of quiz
print("🎉 You've completed the quiz!")
print(f"✅ Your final score is: {quiz.score}/{quiz.question_number}")
