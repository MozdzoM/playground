from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        pass
    else:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_text, text=current_card["French"], fill="black")
        canvas.itemconfig(card_image, image=card_front_img)
        flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)

def learned():
    global current_card
    # print(len(to_learn))
    try:
        to_learn.remove(current_card)
    except ValueError:
        canvas.itemconfig(card_title, text="There are no more cards",  fill="black")
        canvas.itemconfig(card_text, text="Congratulations! 🥳", fill="black")
        canvas.itemconfig(card_image, image=card_front_img)
    else:
        data = pandas.DataFrame(to_learn)
        data.to_csv("./data/words_to_learn.csv", index=False)
        next_card()


# GUI Setup
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
cross_img = PhotoImage(file="./images/wrong.png")
check_img = PhotoImage(file="./images/right.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
unknown = Button(image=cross_img, highlightthickness=0, bd=0, command=next_card)
unknown.grid(row=1, column=0)

known = Button(image=check_img, highlightthickness=0, bd=0, command=learned)
known.grid(row=1, column=1)

next_card()

window.mainloop()
