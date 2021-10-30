from turtle import Screen
from snake import Snake
from food import Food
from score import scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True
snake = Snake()
fod = Food()
scores = scoreboard()

while game_on is True:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.all_turtles[0].distance(fod) < 10:
        fod.refresh()
        scores.scoring()
        snake.add_length()


    if snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].xcor() < -290 or snake.all_turtles[0].ycor() > 290 or snake.all_turtles[0].ycor() < -280:
        scores.score_reset()
        snake.disappear()
        snake.new_snake()

        # get a new snake


    for segment in snake.all_turtles[1:len(snake.all_turtles)]:
        if snake.all_turtles[0].distance(segment) < 5:
            scores.score_reset()
            snake.disappear()
            snake.new_snake()

            # get a new snake to start from the beginning




screen.exitonclick()


