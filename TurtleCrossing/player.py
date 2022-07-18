from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position = (0, -270)
        self.create_player()

    def create_player(self):
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.color("black")
        self.goto(self.starting_position)

    def move(self):
        self.forward(10)

    def goto_home(self):
        self.goto(self.starting_position)

