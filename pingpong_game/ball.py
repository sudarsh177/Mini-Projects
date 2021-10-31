from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.setheading(45)

    def ball_move(self):
        self.forward(5)

    def change_direction(self):
        if self.ycor() < -290 or self.ycor() > 290:
            if self.heading() == 45:
                self.setheading(315)
            elif self.heading() == 135:
                self.setheading(225)
            elif self.heading() == 225:
                self.setheading(135)
            else:
                self.setheading(45)

    def paddle_deflect(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(315)
        else:
            self.setheading(225)




