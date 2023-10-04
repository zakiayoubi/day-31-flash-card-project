from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

word_pair = {}
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")



def next_word():
    global word_pair, flip_timer
    window.after_cancel(flip_timer)
    word_pair = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=word_pair["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    words_to_learn.remove(word_pair)
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=word_pair["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_img)


    


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)


next_word()



window.mainloop()

