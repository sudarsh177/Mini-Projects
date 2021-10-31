from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from display import Display

screen = Screen()
screen.tracer(0)

balls = Ball()
displ = Display()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PING PONG")

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up , "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
near_paddle = False

while game_on:
    time.sleep(0.012)
    balls.ball_move()
    balls.change_direction()
    if left_paddle.distance(balls) < 30:
        if near_paddle is False:
            balls.paddle_deflect()
            displ.incl()
            near_paddle = True

    elif right_paddle.distance(balls) < 30:
        if near_paddle is False:
            balls.paddle_deflect()
            displ.incr()
            near_paddle = True

    elif balls.xcor() > 390 or balls.xcor() < -390:
        displ.game_over()
        game_on = False

    if left_paddle.distance(balls) > 30 and right_paddle.distance(balls) > 30:
        near_paddle = False

    screen.update()


screen.exitonclick()
