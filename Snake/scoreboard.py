from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 370)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 20, 'normal'))

