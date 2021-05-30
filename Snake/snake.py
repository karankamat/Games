from turtle import Turtle
INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_BY = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.head = self.snakebody[0]

    def create_snake(self):
        for pos_i in INITIAL_POS:
            self.add_seg(pos_i)

    def add_seg(self, position):
        snape = Turtle(shape="square")
        snape.penup()
        snape.color("white")
        snape.goto(position)
        self.snakebody.append(snape)

    def extend_seg(self):
        self.add_seg(self.snakebody[-1].position())

    def reset_snake(self):
        for seg in self.snakebody:
            seg.goto(1000, 1000)
        self.snakebody.clear()
        self.create_snake()
        self.head = self.snakebody[0]

    def snake_move(self):
        for seg_i in range((len(self.snakebody) - 1), 0, -1):
            xcor = self.snakebody[seg_i - 1].xcor()
            ycor = self.snakebody[seg_i - 1].ycor()
            self.snakebody[seg_i].goto(xcor, ycor)
        self.snakebody[0].forward(MOVE_BY)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def snake_wall_collision(self):
        if self.snakebody[0].xcor() == 280 or self.snakebody[0].xcor() == -280 \
                or self.snakebody[0].ycor() == 280 or self.snakebody[0].ycor() == -280:
            return True
