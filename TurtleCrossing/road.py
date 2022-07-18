from turtle import Turtle


class Road:
    def __init__(self):
        self.road_width = 300
        self.draw_road()

    def draw_road(self):
        upper = Turtle()
        upper.hideturtle()
        upper.pensize(2)
        upper.penup()
        upper.goto(-300, self.road_width/2)
        upper.pendown()
        upper.goto(300, self.road_width/2)

        lower = Turtle()
        lower.hideturtle()
        lower.pensize(2)
        lower.penup()
        lower.goto(-300, -self.road_width/2)
        lower.pendown()
        lower.goto(300, -self.road_width/2)
