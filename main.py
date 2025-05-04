from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def find_password():
    entered_website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message=" No data file found.")
    else:
        if entered_website in data:
            messagebox.showinfo(title={entered_website},
                                message=f"Email: {data[entered_website]['email']}\npassword :{data[entered_website]['password']}")
        else:
            messagebox.showinfo(title="error", message="No detail for this website exits")


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


def save():
    entered_website = website_entry.get()
    entered_email = email_entry.get()
    entered_password = password_entry.get()
    new_data = {
        entered_website: {
            "email": entered_email,
            "password": entered_password
        }
    }
    if len(entered_password) == 0 or len(entered_website) == 0 or len(entered_email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=12, font=("Arial", 12), command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "fatemepourseif1378@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", width=12, font=("Arial", 12), command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
