from turtle import Turtle, Screen
from player import Player
from road import Road
from cars import Cars
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Crossing")
screen.colormode(255)
screen.tracer(0)

player = Player()
road = Road()
car = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_over = False
loop_counter = 0
while not game_over:
    for n in car.existing_cars:
        if player.distance(n) < 25:
            game_over = True
            scoreboard.game_over()

    if player.ycor() > 170:
        scoreboard.update()
        player.goto_home()
        car.increase_speed()

    if loop_counter % 600 == 0:
        car.generate()
    car.move()
    screen.update()
    loop_counter += 1

screen.exitonclick()
