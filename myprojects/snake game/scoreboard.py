from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # Always find data.txt relative to this file
        dir_path = os.path.dirname(__file__)
        self.file_path = os.path.join(dir_path, "data.txt")

        try:
            with open(self.file_path, mode="r") as data:
                self.high_score = int(data.read())
        except (IOError, ValueError):
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_path, mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        








