from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def incscore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)
    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
