from tkinter import *
import pandas
import random

data = pandas.read_csv("KoreanWords.csv")
words = data.to_dict(orient="records")


def next_card():
    new_word = random.choice(words)

    for key, value in new_word.items():
        if key == "Korean":
            card.itemconfig(language, text=f"{key}", font=('Ariel', 40, 'italic'))
            card.itemconfig(word, text=f"{value}", font=('fixed', 60, 'bold'))


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Korean/English Flashcards")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

card = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card.create_image(400, 263, image=card_front_image)
card.config(background=BACKGROUND_COLOR, highlightthickness=0)
language = card.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
word = card.create_text(400, 263, text="Word", font=('Ariel', 60, 'bold'))
card.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card, borderwidth=0)
right_button.grid(row=1, column=1)

window.mainloop()
