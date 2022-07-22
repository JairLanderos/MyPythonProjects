import turtle
import pandas
from turtle import Turtle, Screen

states = pandas.read_csv("mexico_states.csv")
state_name_list = states.state.to_list()

screen = Screen()
screen.title("Mexico States Game")

mexico_map = "Mexico.gif"
screen.addshape(mexico_map)

turtle.shape(mexico_map)

game_over = False
guessed_states = []
while len(guessed_states) < 32:
    answer_state = screen.textinput(f"Type a state name ({len(guessed_states)}/32)",
                                    prompt="What's another state name?").title()
    if answer_state in state_name_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        name = Turtle()
        name.hideturtle()
        name.penup()
        state_info = states[states.state == answer_state]
        name.goto(int(state_info.x), int(state_info.y))
        name.write(answer_state, align="center", font=('Courier', 5, 'normal'))

screen.exitonclick()
