from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# Setting the background colour
screen.bgcolor("black")
# Giving a title to the screen
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="s", fun=snake.move_down)

flag = True
while flag:
    screen.update()
    time.sleep(0.25)
    if snake.snake_wall_collision():
        snake.reset_snake()
        score.reset_score()
    else:
        snake.snake_move()

    if snake.head.distance(food) < 11:
        food.refresh()
        snake.extend_seg()
        score.increase()

    for segment in snake.snakebody[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            score.reset_score()

screen.exitonclick()
