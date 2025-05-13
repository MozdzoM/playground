import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (
        [choice(letters) for _ in range(randint(8, 10))] +
        [choice(symbols) for _ in range(randint(2, 4))] +
        [choice(numbers) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset_entries():
    website_entry.delete(0, END)
    login_entry.delete(0, END)
    password_entry.delete(0, END)

    website_entry.focus()
    login_entry.insert(0, "email@gmail.com")

def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo("Error", "You need to enter a website first")
    else:
        try:
            with open("data.json") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
            messagebox.showinfo("Error", "No data found")
        else:
            for site in data:
                if site.lower() == website.lower():
                    credentials = data[site]
                    messagebox.showinfo(f"{site} Credentials",
                                        f"Your credentials for {site}:\n"
                                        f"Login: {credentials['email']}\n"
                                        f"Password: {credentials['password']}")
                    return
            messagebox.showinfo("Not Found", f"No credentials found for {website}")

def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": login,
            "password": password,
        }
    }

    if len(website) == 0 or len(login) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please fill all the fields")
    else:
        try:
            with open("data.json", "r") as password_file:
                # Read old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("data.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            # Update old data
            data.update(new_data)

            with open("data.json", "w") as password_file:
                # Save updated data
                json.dump(data, password_file, indent=4)
        finally:
                reset_entries()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(240, 240)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# Frames
website_frame = Frame(window)
website_frame.grid(column=1, row=1, columnspan=2, sticky="W")
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2, sticky="W")

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(website_frame, width=17)
website_entry.focus()
website_entry.grid(column=0, row=0, padx=(0, 6))

login_entry = Entry(width=35)
login_entry.insert(0, "email@gmail.com")
login_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(password_frame, width=17)
password_entry.grid(column=0, row=0, padx=(0, 6))

# Buttons
search_button = Button(website_frame, text="Search", width=13,
                        command=search,
                        bd=0, highlightthickness=0, padx=2, pady=2)
search_button.grid(column=1, row=0)

generate_button = Button(password_frame, text="Generate Password",
                        command=generate_password,
                        bd=0, highlightthickness=0, padx=2, pady=2)
generate_button.grid(column=1, row=0)

add_button = Button(text="Add", width=32, command=save,
                    bd=0, highlightthickness=0, padx=2, pady=2)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
