from snake import Snake
import turtle
import time

playing = True

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Snake")
window.bgcolor("black")
window.tracer(0)  # turn off so image doesn't auto update


snake = Snake()  # create new snake object
window.listen()
window.onkey(snake.up,"Up")
window.onkey(snake.down,"Down")
window.onkey(snake.left,"Left")
window.onkey(snake.right, "Right")

while playing:
    window.update()
    time.sleep(0.1)
    snake.move()

window.exitonclick()
