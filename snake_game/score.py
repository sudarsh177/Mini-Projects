from turtle import Turtle


class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../../../../../../Desktop/high_socre.txt", mode= "r") as high:
            self.highscore = int(high.read())
        self.color("White")
        self.penup()
        self.sety(280)
        self.hideturtle()
        self.scoring()
        self.clear()
        self.display()


    def scoring(self):
        self.score += 1
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score - 1
        with open("../../../../../../../Desktop/high_socre.txt", mode="w") as high:
            high.write(str(self.highscore))
        self.display()


    def score_reset(self):
        self.clear()
        self.score = 1
        self.display()

    def display(self):
        self.write(f"Score: {self.score - 1} High Score: {self.highscore}", align='center', font=('Courier', 12, 'normal'))







