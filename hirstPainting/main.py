import random
from turtle import Turtle, Screen
colorList = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turty = Turtle()
turty.penup()
turty.goto(-270, -300)
turty.pendown()
turty.hideturtle()
turty.pensize(20)
turty.speed("fastest")
turty.screen.colormode(255)
def getColor(clist):
    index = random.randint(0,29)
    color = clist[index]
    index += 1
    turty.color(color)
def drawX():
    for i in range (0, 10):
        getColor(colorList)
        turty.forward(1)
        turty.penup()
        turty.forward(55)
        turty.pendown()

for i in range (0,10):
    drawX()
    turty.penup()
    y = turty.ycor() + 50
    turty.goto(-270, y)
    turty.pendown()

screen = Screen()
screen.exitonclick()