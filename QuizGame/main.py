from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from gui import QuizInterface

question_bank = []
for question in range(len(question_data)):
    question_bank.append(Question(question_data[question]["question"], question_data[question]["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
