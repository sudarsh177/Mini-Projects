from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.goto(250,0)
        self.write("GAME OVER", align='center', font=('Courier', 18, 'normal'))
