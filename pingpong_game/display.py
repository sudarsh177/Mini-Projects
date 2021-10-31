from turtle import Turtle

class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.home()
        self.color("white")
        # self.goto(0, 250)
        self.l_score = 0
        self.r_score = 0
        # self.write("Score", align='center', font=('Courier', 18, 'normal'))
        self.goto(-50, 240)
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(50, 240)
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=('Courier', 18, 'normal'))

    def incl(self):
        self.goto(-50, 240)
        self.l_score += 1
        self.clear()
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(50, 240)
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))

    def incr(self):
        self.goto(50, 240)
        self.r_score += 1
        self.clear()
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(-50, 240)
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))










