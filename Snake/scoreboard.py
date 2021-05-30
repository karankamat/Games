from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_from_file()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.display_score()

    def reset_score(self):
        outfile = open("HighScore.txt", "w")
        outfile.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    @staticmethod
    def read_from_file():
        high_score = 0
        with open("HighScore.txt") as readfile:
            content = readfile.readlines()
        for line in content:
            high_score = line[0]
        return int(high_score)
