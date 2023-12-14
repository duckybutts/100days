import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
playing = True

textTurty = turtle.Turtle()

while playing:
    userAnswer = screen.textinput(title=f"States Named = {score}/50", prompt="Name a State").title()
    data = pandas.read_csv("50_states.csv")

    for state in data.state:
        if userAnswer == state:
            score += 1
            state_row = data[data["state"] == userAnswer].iloc[0]
            textTurty.hideturtle()
            textTurty.penup()
            textTurty.goto(state_row[1], state_row[2])
            textTurty.pendown()
            textTurty.write(f"{state}")
            screen.update()

    if score == 50:
        screen.clear()
        messagebox.showinfo(title= "aye", message = "congrats")
        playing = False





