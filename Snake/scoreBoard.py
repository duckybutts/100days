from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font = ("Courier", 24, "normal"))


    def incScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font = ("Courier", 24, "normal"))

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))
