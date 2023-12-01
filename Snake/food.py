from turtle import Turtle
import random 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # make 10x10
        self.color("lightblue")
        self.speed("fastest") 
        self.refresh()

    def refresh(self):
        randomx = random.randint(-270, 280)
        randomy = random.randint(-270, 280)
        self.goto(randomx, randomy)