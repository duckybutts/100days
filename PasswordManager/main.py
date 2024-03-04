from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    websiteStuff = inputWeb.get()
    emailStuff = inputEmail.get()
    passwordStuff = inputPassword.get()

    if websiteStuff == "" or emailStuff == "" or passwordStuff == "" :
        messagebox.showinfo(title="Empty Fields", message="Don't leave any fields empty.")
    else :
        isOkay = messagebox.askokcancel(title=f"\n {websiteStuff}", message= f"Input Values: \n {emailStuff} \n {passwordStuff}  \n  Are these correct? " )
        if isOkay :
            with open("data.txt", "a") as datafile:
                datafile.write(f"{websiteStuff} | {emailStuff} | {passwordStuff} \n")
        inputWeb.delete(0, END)
        inputEmail.delete(0, END)
        inputPassword.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordLetters = [random.choice(letters) for letter in range(random.randint(8,10))]
    passwordNumbers = [random.choice(numbers) for letter in range(random.randint(2,4))]
    passwordSymbols = [random.choice(symbols) for letter in range(random.randint(2,4))]

    password = passwordLetters + passwordSymbols + passwordNumbers

    shuffle = list(password)
    random.shuffle(shuffle)
    password = ''.join(shuffle)

    inputPassword.delete(0, END)
    inputPassword.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady=20, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
passwordImg = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=passwordImg)
canvas.grid(column=1, row=0)
site = Label(text= "Website:",highlightbackground="white", bg="white", fg="black")
site.grid(column=0, row=1)
inputWeb = Entry(width=35, highlightbackground="white", bg="white", fg="black")
inputWeb.focus()  # auto set cursor to first field on open
inputWeb.grid(column=1, row=1, columnspan=2)
email = Label(text= "Email/Username:",highlightbackground="white", bg="white",fg="black")
email.grid(column=0, row=2)
inputEmail = Entry(width=35, highlightbackground="white", bg="white", fg="black")
inputEmail.grid(column=1, row=2, columnspan=2)
inputEmail.insert(0, "duckyrshannon@gmail.com")
password = Label(text= "Password:",highlightbackground="white", bg="white",fg="black")
password.grid(column=0, row=3)
inputPassword = Entry(width=21, highlightbackground="white", bg="white", fg="black")
inputPassword.grid(column=1, row=3)
generatePassword = Button(text="Generate Password", command=generate,  highlightbackground="white", bg="white")
generatePassword.grid(column=2, row=3)
add = Button(text="Add", command=add,  highlightbackground="white", width=36)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()