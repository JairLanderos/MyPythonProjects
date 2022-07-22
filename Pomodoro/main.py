from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
state = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global state

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    state = 0
    start_button["state"] = "active"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global state
    start_button["state"] = "disabled"

    if state % 2 == 0:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN)
        state += 1
    elif state == 1 or state % 3 == 0 or state % 5 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN)
        state += 1
    elif state % 7 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN)
        state = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = str(math.floor(count / 60)).zfill(2)
    seconds = str(count % 60).zfill(2)
    count_string = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=count_string)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=100, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 60, 'bold'), background=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_image = PhotoImage(file="check.png")
check_label = Label(image=check_mark_image, background=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()
