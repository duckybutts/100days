import turtle
import random


colors = ["red", "orange", "grey", "green", "blue", "purple"]

racing = False
screen = turtle.Screen()
screen.setup(width=500,height=400)
userBet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtleList = []
def step(turtle):
    speed = random.randint(1, 10)
    turtle.speed(speed)
    turtle.forward(10)

y=-120

for turtles in range (0, 6):
    newTurtle = turtle.Turtle(shape="turtle")
    newTurtle.color(colors[turtles])
    newTurtle.penup()
    newTurtle.goto(x=-220, y=y)
    y = y + 45
    turtleList.append(newTurtle)


if userBet:
    racing = True

while racing:

    for turtle in turtleList:
        if turtle.xcor() > 230:
            racing = False
            winner = turtle.pencolor()
            if winner == userBet:
                print(f"You won! The winning turtle was {winner}")
            else:
                print(f"You lost. The winning turtle was {winner}.")

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()