from turtle import Turtle, Screen

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Facing upward

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        x = self.xcor() - MOVE_DISTANCE
        if x > -380:  # left boundary
            self.setx(x)

    def go_right(self):
        x = self.xcor() + MOVE_DISTANCE
        if x < 380:  # right boundary
            self.setx(x)

   

