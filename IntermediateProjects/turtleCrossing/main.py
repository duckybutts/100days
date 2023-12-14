import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
cars = []
count = 0
score = 0
level = 0
num = 5
player = Player()
scoreboard = Scoreboard()
def resetscreen():
    screen.tracer(0)
    while len(cars) < 20:  # place some cars to start
        car = CarManager()
        car.randomizePosition()
        car.increaseSpeed(level)
        cars.append(car)

resetscreen()
game_is_on = True
while game_is_on:

    screen.listen()
    screen.onkey(player.move, "Up")

    if player.ycor() > 280:
        cars = []
        level += 1
        if num > 0:
            num = num -1
        screen.clear()
        resetscreen()
        player = Player()
        scoreboard.incscore()

    for car in cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.gameover()

    count += 1
    if count % num == 0:
        car = CarManager()
        cars.append(car)
        car.increaseSpeed(level)
    for car in cars:
        car.move()

    time.sleep(0.03)
    screen.update()

screen.exitonclick()