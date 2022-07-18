from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)

question_bank = []
for question in range(len(question_data)):
    question_bank.append(Question(question_data[question]["text"], question_data[question]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
