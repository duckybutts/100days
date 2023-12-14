from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
movedistance = 3
increment = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 2)
        self.color(self.generateColor())
        self.penup()
        self.goto(300, self.generatePosition())
        self.moveDistance = movedistance

    def generateColor(self):
        number = random.randint(0,5)
        return COLORS[number]

    def generatePosition(self):
        returnValue = 0
        while returnValue == 0:
            number = random.randint(-240, 240)
            if number % 10 == 0:
                returnValue = number
        return returnValue

    def move(self):
        xCor = self.xcor()
        yCor = self.ycor()
        xCor -= self.moveDistance
        self.goto(xCor, yCor)

    def randomizePosition(self):
        self.goto(self.generatePosition(), self.generatePosition())

    def increaseSpeed(self, level):
        self.moveDistance += (level * increment)

