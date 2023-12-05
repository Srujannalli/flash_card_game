from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

try:
    pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global french_text, flip_timer
    window.after_cancel(flip_timer)
    french_text = random.choice(data_dict)
    canvas.itemconfig(text_up, text="French")
    canvas.itemconfig(text_bottom, text=french_text["French"], fill="black")
    canvas.itemconfig(text_bottom, text=french_text["French"], fill="black")
    canvas.itemconfig(canvas_image, image=pic)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=new_Pic)
    canvas.itemconfig(text_up, text="English")
    canvas.itemconfig(text_bottom, text=french_text["English"])


def known():
    data_dict.remove(french_text)
    print(len(data_dict))
    known_data = pandas.DataFrame(data_dict)
    known_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0)
pic = PhotoImage(file="images/card_front.png")
new_Pic = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=pic)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_pic, command=next_card)
wrong_button.grid(column=0, row=1, padx=50)
right_pic = PhotoImage(file="images/right.png")
right_button = Button(image=right_pic, command=known)
right_button.grid(column=1, row=1, padx=50)
text_up = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text_bottom = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

next_card()

window.mainloop()