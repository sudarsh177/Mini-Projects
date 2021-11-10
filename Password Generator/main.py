from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search_word():
    try:
        with open("new.json", "r") as cred:
            data = json.load(cred)
            not_found = True
            web = website_entry.get()
            for entry in data:
                if entry == web:
                    not_found = False
                    messagebox.showwarning(web, f'''Email: {data[entry]["email"]}\nPassword: {data[entry]["password"]}''')
                    break
                else:
                    not_found = True


            if not_found is True:
                messagebox.showwarning(web, f"Credentials not found")

    except FileNotFoundError:
        messagebox.showwarning("Warning", f"No file found")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    password= "".join(password_list)

    password_label_output.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():

    wb = website_entry.get()
    em = username_entry.get()
    pa = password_label_output.get()

    new_data = {
        wb: {
            "email" : em,
            "password" : pa
        }
    }

    if wb == "" or pa == "":
        messagebox.showwarning("Warning", "Please do not leave the field(s) empty")

    else:
        okay = messagebox.askokcancel(title= wb, message=f"You have entered: \n\nWebsite: {wb}\nEmail: {em}\nPassword: {pa}\n")

        if okay:
            try:
                with open("new.json", "r") as cred:
                    data = json.load(cred)
                    data.update(new_data)

            except FileNotFoundError:
                with open("new.json","w") as cred:
                    json.dump(new_data, cred,indent = 4)

            else:
                with open("new.json","w") as cred:
                    json.dump(data, cred,indent = 4)

            website_entry.delete(0, END)
            password_label_output.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx = 70, pady = 70)

canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)

website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

username_label = Label(text = "Email/Username:")
username_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

website_entry = Entry(width = 33)
website_entry.grid(column = 1, row = 1)
website_entry.focus()

username_entry = Entry(width = 52)
username_entry.grid(column = 1, row = 2, columnspan = 2 )
username_entry.insert(0, "xyz@gmail.com")

password_label_output = Entry(width = 33)
password_label_output.grid(column = 1, row = 3)

generate_button = Button(text = "Generate Password",command = gen_password)
generate_button.grid(column = 2, row = 3)

search_button = Button(text = "Search", width = 14,command = search_word)
search_button.grid(column = 2, row = 1)

add_button = Button(text = "Add", width = 44, command = save_file)
add_button.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()

