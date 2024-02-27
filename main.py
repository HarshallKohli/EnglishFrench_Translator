from tkinter import *
import pandas
import random

# constants
LIGHT_BLUE = "#9BB8CD"
language_font = ("Ariel", 40, "italic")
word_font = ("Ariel", 60, "bold")
current_word = {}
to_learn = {}

# TODO : Creating New Flash Cards
try:
    data1 = pandas.read_csv("flash-card-project-start/data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
else:
    to_learn = data1.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_lang_name, text="French", fill="black")
    canvas.itemconfig(card_words_name, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_front, image=card_front_image)
    flip_timer = window.after(3500, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_front, image=card_back_image)
    canvas.itemconfig(card_words_name, text=current_word["English"], fill="white")
    canvas.itemconfig(card_lang_name, text="English", fill="white")


# def show_english_translation():
#     canvas.itemconfig(canvas_front, image=card_back_image)
#     canvas.itemconfig(card_words_name, text=current_word["English"], fill="white")
#     canvas.itemconfig(card_lang_name, text="English", fill="white")


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()
# index=false as to not repeat indexing in csv file

# TODO : CREATING THE USER INTERFACE


window = Tk()
window.title("Flashy French")
window.config(padx=50, pady=50, bg=LIGHT_BLUE)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="flash-card-project-start/images/card_back.png")
canvas_front = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=LIGHT_BLUE, highlightthickness=0)


card_lang_name = canvas.create_text(400, 150, text="", font=language_font)
card_words_name = canvas.create_text(400, 263, text="", font=word_font)

canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
idk_button = Button(image=cross_image, highlightthickness=0, command=flip_card)
(idk_button.grid(row=1, column=0))

tick_image = PhotoImage(file="flash-card-project-start/images/right.png")
know_it_button = Button(image=tick_image, highlightthickness=0, command=is_known)
know_it_button.grid(row=1, column=1)

next_card()

window.mainloop()
