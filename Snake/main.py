from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def move_up():
    snake.snake_segments[0].seth(90)


snake_heading_offset = {
    0: {"x": 20, "y": 0},
    90: {"x": 0, "y": 20},
    270: {"x": 0, "y": -20}
}

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.snake_segments[0].xcor() > (screen.window_width()/2 - 10) or \
            snake.snake_segments[0].xcor() < (-screen.window_width()/2 + 10) or \
            snake.snake_segments[0].ycor() > (screen.window_height()/2 - 10) or \
            snake.snake_segments[0].ycor() < (-screen.window_height()/2 + 10):
        game_over = True
        scoreboard.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
