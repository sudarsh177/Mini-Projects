from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.score = 1
        self.hideturtle()
        self.goto(-220, 230)
        self.write(f"Level: 1", align= 'center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align='center', font=FONT)




