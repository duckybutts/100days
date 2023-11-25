import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """ Creates snake object """
    def __init__(self):
        self.segments = []
        self.xPos = -60
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates a new 3 segment snake"""
        for i in range(0, 3):
            newSnake = turtle.Turtle("square")
            newSnake.goto(x=self.xPos, y=0)
            newSnake.color("white")
            newSnake.penup()
            self.xPos += 20
            self.segments.append(newSnake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[i - 1].xcor()
            newY = self.segments[i - 1].ycor()
            self.segments[i].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


