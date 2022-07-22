from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_text = Canvas(width=300, height=250, background="white")
        self.text = self.question_text.create_text(150, 125, width=280,
                                                   text="Some random question",
                                                   font=('Arial', 20, 'italic'))
        self.question_text.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.show_question()

        self.window.mainloop()

    def show_question(self):
        if self.quiz.still_has_questions():
            self.question_text.config(background="white")
            question_text = self.quiz.next_question()
            self.question_text.itemconfig(self.text, text=question_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.question_text.config(background="yellow")
            self.question_text.itemconfig(self.text, text="GAME OVER")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.question_text.config(background="green")
        else:
            self.question_text.config(background="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.show_question)




