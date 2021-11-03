from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.level = 0
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)


    def move(self):
        self.forward(MOVE_DISTANCE)


    def reset_position(self):
        self.goto(STARTING_POSITION)







