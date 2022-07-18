from turtle import Turtle
import random


class Cars:
    def __init__(self):
        self.speed = 0.05
        self.existing_cars = []
        self.generate()

    def generate(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(self.random_color())
        car.penup()
        car.speed("slowest")
        car.seth(180)
        car.goto(310, random.randint(-145, 145))
        self.existing_cars.append(car)

    def move(self):
        for car in self.existing_cars:
            car.forward(1 * self.speed)
            if -290 > car.xcor():
                car.clear()
                car.hideturtle()

        self.existing_cars = [car for car in self.existing_cars if car.xcor() > -300]

    def increase_speed(self):
        self.speed += 0.025


    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return tuple((r, g, b))
