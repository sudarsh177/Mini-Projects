from turtle import Screen, Turtle
class Snake:

    def __init__(self):
        self.all_turtles = []
        self.screen = Screen()
        self.prev = (0, 0)
        for a in range(3):
            joe = Turtle(shape = "square")
            joe.penup()
            joe.goto(0 - (20 * a), 0)
            joe.color("white")
            self.all_turtles.append(joe)

    def move(self):
        def move_up():
            if self.all_turtles[0].heading() == 90 or self.all_turtles[0].heading() == 270:
                pass
            else:
                self.all_turtles[0].setheading(90)

        def move_right():
            if self.all_turtles[0].heading() == 0 or self.all_turtles[0].heading() == 180:
                pass
            else:
                self.all_turtles[0].setheading(0)

        def move_left():
            if self.all_turtles[0].heading() == 0 or self.all_turtles[0].heading() == 180:
                pass
            else:
                self.all_turtles[0].setheading(180)

        def move_down():
            if self.all_turtles[0].heading() == 90 or self.all_turtles[0].heading() == 270:
                pass
            else:
                self.all_turtles[0].setheading(270)

        self.screen.listen()

        self.screen.onkey(move_up, "Up")
        self.screen.onkey(move_down, "Down")
        self.screen.onkey(move_left, "Left")
        self.screen.onkey(move_right, "Right")

        self.prev = self.all_turtles[0].pos()
        self.all_turtles[0].forward(10)

        for a in range(1, len(self.all_turtles)):
            cur = self.all_turtles[a].pos()
            self.all_turtles[a].goto(self.prev)
            self.prev = cur


    def add_length(self):
        joe = Turtle(shape="square")
        joe.color("white")
        joe.penup()
        joe.goto(self.prev)
        self.all_turtles.append(joe)

    def new_snake(self):
        self.all_turtles.clear()
        self.prev = (0, 0)
        for a in range(3):
            joe = Turtle(shape="square")
            joe.penup()
            joe.goto(0 - (20 * a), 0)
            joe.color("white")
            self.all_turtles.append(joe)

    def disappear(self):
        for a in range(0,len(self.all_turtles)):
            self.all_turtles[a].goto(310,310)








