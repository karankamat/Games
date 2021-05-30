from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_food = random.choice(range(-280, 280, 20))
        y_food = random.choice(range(-280, 280, 20))
        self.goto(x_food, y_food)
