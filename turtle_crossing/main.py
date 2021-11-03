import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()

screen.listen()
screen.onkey(tim.move, "Up")
carclass = CarManager()
disp = Scoreboard()

n = 0
game_is_on = True
count = 0
carclass.create_car()
while game_is_on:
    count += 1
    time.sleep(0.05 - n)
    if count == 6:
        carclass.create_car()
        count = 0
    carclass.move()

    for entries in carclass.all_turtles:
        if tim.distance(entries) < 20:
            game_is_on = False
            disp.game_over()

    if tim.ycor() > 280:
        n += 0.01
        tim.level += 1
        tim.reset_position()
        disp.increase_score()

    screen.update()


screen.exitonclick()
