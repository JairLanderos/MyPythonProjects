from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("My Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_over = False
while not game_over:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left_score += 1
        scoreboard.update()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.right_score += 1
        scoreboard.update()
        ball.reset()

screen.update()

screen.exitonclick()
