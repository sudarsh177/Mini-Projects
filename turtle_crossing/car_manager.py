from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_turtles = []



    def create_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(310, random.randint(-250, 250))
        self.all_turtles.append(car)




    def move(self):
        for entries in self.all_turtles:
            entries.backward(STARTING_MOVE_DISTANCE)













