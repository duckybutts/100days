from snake import Snake
import turtle
import time
from food import Food
from scoreBoard import ScoreBoard

playing = True
window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Snake")
window.bgcolor("black")
window.tracer(0)  # turn off so image doesn't auto update
counter =0

snake = Snake()  # create new snake object
food = Food()
scoreBoard = ScoreBoard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

while playing:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreBoard.incScore()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        playing = False
        scoreBoard.gameOver()

    for segment in snake.segments:
        if (segment != snake.head and segment != snake.segments[1] and segment != snake.segments[2] and
                snake.head.distance(segment) < 10):
            playing = False
            scoreBoard.gameOver()

window.exitonclick()
