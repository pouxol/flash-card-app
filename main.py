from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
sel_element = {}

try:
    french_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pd.read_csv("data/french_words.csv")
finally:
    french_words_dict = french_words.to_dict(orient="records")


def new_word():
    global sel_element, timer
    window.after_cancel(timer)
    sel_element = random.choice(french_words_dict)
    sel_0_lang = list(sel_element.keys())[0]
    sel_0_word = sel_element[sel_0_lang]

    canvas.itemconfig(canvas_lang, text=sel_0_lang, fill="#000000")
    canvas.itemconfig(canvas_word, text=sel_0_word, fill="#000000")
    timer = window.after(3000, func=flip_card)


def is_known():
    french_words_dict.remove(sel_element)
    df = pd.DataFrame(french_words_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_word()


def flip_card():
    sel_1_lang = list(sel_element.keys())[1]
    sel_1_word = sel_element[sel_1_lang]

    canvas.itemconfig(canvas_lang, text=sel_1_lang, fill="#ffffff")
    canvas.itemconfig(canvas_word, text=sel_1_word, fill="#ffffff")
    canvas.itemconfig(canvas_image, image=card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_lang = canvas.create_text(400, 150, text="language", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=is_known, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=new_word, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0)

new_word()

window.mainloop()
