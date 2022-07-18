from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", align="center", font=('Courier', 20, 'normal'))

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 200)
        self.write("GAME OVER", align="center", font=('Courier', 20, 'normal'))