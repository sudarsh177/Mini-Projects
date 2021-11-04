from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(500, 400)
choice = screen.textinput(title="User Bet", prompt="Which turtle is going to win?")
colour = ["red", "blue", "green", "orange", "pink", "black"]

pos = -80
turtle_collection = []
for a in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, pos + (40*a))
    tim.color(colour[a])
    turtle_collection.append(tim)

if choice:
    race_on = True


while race_on is True:
    for a_turtle in turtle_collection:
        if a_turtle.xcor() > 230:
            race_on = False
            winner = a_turtle.pencolor()
            if choice == winner:
                print("You've won the race!")
            else:
                print(f"You've lost. The winner is {winner}")


        a_turtle.forward(random.randint(1, 10))


                         

screen.exitonclick()
