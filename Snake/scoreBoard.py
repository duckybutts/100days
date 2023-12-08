from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open("data.txt", mode="r") as file:
            self.highScore = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score} Highscore: {self.highScore}", align="center", font = ("Courier", 24, "normal"))


    def incScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highScore}", align="center", font = ("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highScore}")

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highScore}", align="center", font = ("Courier", 24, "normal"))

