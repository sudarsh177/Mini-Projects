import random
from tkinter import  *
import pandas
word = "same"
num = 0
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("new_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    print("File not found")
data_dict = data.to_dict(orient= "records")
added_words = []


def change_to_english(arg):
    flash.itemconfig(back_img, image = back_card)
    flash.itemconfig(language_text, text="English")
    flash.itemconfig(word_text, text=arg)


def right_click():
    global num
    change_word()
    data_dict.remove(data_dict[num])
    dataframe = pandas.DataFrame(data_dict)
    dataframe.to_csv("new_words.csv")

def change_word():
    global num
    flash.itemconfig(back_img, image= tomato_img)
    num = random.randint(1, len(data_dict)-1)
    french_word = data_dict[num]["French"]
    english_word = data_dict[num]["English"]

    if french_word in added_words:
        change_word()

    else:
        added_words.append(french_word)
        flash.itemconfig(language_text, text="French")
        flash.itemconfig(word_text, text = french_word)
        window.after(3000, change_to_english, english_word)


window = Tk()
window.title("Flash Card")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)


flash = Canvas(width = 800, height = 526,bg = BACKGROUND_COLOR, highlightthickness = 0)
tomato_img = PhotoImage(file = "card_front.png")
back_card = PhotoImage(file = "card_back.png")
back_img = flash.create_image(400, 263, image = tomato_img )
flash.grid(column = 0, row =0 , columnspan = 2)
language_text = flash.create_text(400,150, text = "French" , fill = "black", font = ("Arial", 40, "italic"))
word_text = flash.create_text(400,263, text = "Word", fill = "black", font = ("Arial", 60,"bold"))

red_button = PhotoImage(file ="wrong.png" )
wrong = Button(image = red_button, highlightthickness = 0,command = change_word)
wrong.grid(column = 0, row =1)

green_button = PhotoImage(file ="right.png")
right = Button(image = green_button, highlightthickness = 0,command = right_click)
right.grid(column = 1, row =1)


window.mainloop()
