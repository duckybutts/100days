import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")

def chooseColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def drawSpirograph(sizeOfGap):
    for i in range(int(360 / sizeOfGap)):
        timmy.color(chooseColor())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)

drawSpirograph(5)

screen = Screen()
screen.exitonclick()
