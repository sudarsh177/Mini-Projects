from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, place):
        super().__init__()
        self.penup()
        self.color("white")
        self.left(90)
        self.shape("square")
        self.goto(place)
        self.shapesize(stretch_len=5, stretch_wid=1)


    def move_up(self):
        self.forward(30)


    def move_down(self):
        self.backward(30)

