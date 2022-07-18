import random
import turtle as t
from turtle import Turtle, Screen


def draw_goal_line(offset):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x=230, y=-offset-30)
    line.pendown()
    line.left(90)
    line.width(5)
    line.speed("fastest")
    while line.ycor() != (offset + 30):
        line.forward(10)


def set_road(offset, turtles_number):
    height = screen.window_height()
    draw_goal_line(offset)
    if (2 * offset) >= height:
        print("Offset is too large. Couldn't set the road.")
        return
    road_width = height - (2 * offset)
    if turtles_number < 2:
        print("There must be at least 2 turtles. Could not set the road")
        return
    turtles_distance = road_width / (turtles_number - 1)
    participants = []
    for turtle in range(turtles_number):
        participants.append(Turtle(shape="turtle"))
        participants[turtle].penup()
        participants[turtle].goto(y=(((-height/2) + offset) + (turtle * turtles_distance)), x=-230)
        participants[turtle].color(colors[turtle])
        participants[turtle].speed("slowest")
    return participants


t.colormode(255)
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]

is_race_on = False

players_number = 4

players = set_road(100, players_number)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in players:
        turtle.forward(random.randint(1, 5))
        if turtle.xcor() >= 220:
            is_race_on = False
            winner = turtle

for index in range(players_number):
    if players[index] == winner:
        winner_index = index

if colors[winner_index] != user_bet:
    print("Your turtle did not win.")
else:
    print("You win")

screen.exitonclick()
