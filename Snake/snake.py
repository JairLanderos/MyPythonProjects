from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_segments = []
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        head_pos = self.snake_segments[0].pos()
        self.snake_segments[-1].goto(head_pos)
        tail = self.snake_segments.pop()
        self.snake_segments.insert(1, tail)
        self.snake_segments[0].forward(20)

    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)



