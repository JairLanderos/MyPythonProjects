from tkinter import messagebox
from tkinter import *
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ==============================================================================================
#                                FIND EXISTING INFORMATION
# ==============================================================================================

def find_password():
    website = website_entry.get()
    if website == "":
        messagebox.showerror(title="Password Manager", message="Enter a website name to search.")
        return

    try:
        with open("data.json", mode='r') as data:
            content = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Password Manager", message="No data available.")
    else:
        for key in content:
            if website == key:
                string = f"Email/Username: {content[key]['Email/Username']}\nPassword: {content[key]['Password']}"
                messagebox.showinfo(title="Password Manager", message=string)
                return
        messagebox.showwarning(title="Password Manager", message="No details for the website exists.")


# ==============================================================================================
#                                GENERATION OF A RANDOM PASSWORD
# ==============================================================================================

def generate_password():
    password_list = []
    password = ""

    password_entry.delete(0, END)

    for n in range(4):
        password_list.append(random.choice(letters))

    for n in range(4):
        password_list.append(random.choice(numbers))

    for n in range(2):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    for char in password_list:
        password += char

    password_entry.insert(0, password)


# ==============================================================================================
#                                SAVE THE INFORMATION ENTERED
# ==============================================================================================

def get_entries():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "Email/Username": username,
            "Password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Password Manager", message="Please fill in all fields.")
        return

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    try:
        with open("data.json", mode='r') as data:
            content = json.load(data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("data.json", mode='w') as data:
            json.dump(new_dict, data, indent=4)
    else:
        content.update(new_dict)

        with open("data.json", mode='w') as data:
            json.dump(content, data, indent=4)

    messagebox.showinfo(title="Password Manager", message="Information saved successfully.")


# ==============================================================================================
#                                   CREATION OF THE GUI
# ==============================================================================================

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background='white')

padlock_logo = Canvas(width=200, height=200, background='white', highlightthickness=0)
padlock_image = PhotoImage(file="padlock.png")
padlock_logo.create_image(100, 100, image=padlock_image)
padlock_logo.grid(row=0, column=1)

website_label = Label(text="Website:", font=('Courier', 15, 'normal'), background="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)

username_label = Label(text="Email/Username:", font=('Courier', 15, 'normal'), background="white")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:", font=('Courier', 15, 'normal'), background="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=get_entries)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
