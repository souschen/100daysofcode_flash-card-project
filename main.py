from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

current_card = {}
Title = "French"
word = "is gay"
Title_front = "French"
word_front = "is gay"
FONT_title = ("Ariel", 40, "italic")
FONT_word = ("Ariel", 60, "bold")
timer = None


# ___________________________ Action____________________________________#


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    print(to_learn)
    learn_word = current_card["French"]
    card_img.config(file='images/card_front.png')
    card.itemconfig(title_text_front, text=Title_front, fill="black")
    card.itemconfig(word_text_front, text=learn_word, fill="black")
    window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    card_img.config(file='images/card_back.png')
    card.itemconfig(title_text_front, text="English", fill="white")
    card.itemconfig(word_text_front, text=current_card["English"], fill="white")


# ___________________________ UI ____________________________________#


window = Tk()
window.title("Flashcard project")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file='images/card_front.png')
card.create_image(400, 270, image=card_img)
title_text_front = card.create_text(400, 150, text=Title_front, fill="black", font=FONT_title)
word_text_front = card.create_text(400, 263, text=word_front, fill="black", font=FONT_word)
card.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
