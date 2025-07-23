import turtle as t
import random

# Create turtle object
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# timmy_the_turtle.left(180)
#
# for _ in range(5):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
# Allow RGB values from 0 to 255
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")
# timmy_the_turtle.speed('fast')
#
# for _ in range(1000):
#     timmy_the_turtle.color(color())
#     timmy_the_turtle.forward(25)
#     timmy_the_turtle.setheading(random.choice(directions))

# Timmy_the_Turtle draws a spirograph

for _ in range(999):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.forward(2)
    timmy_the_turtle.left(25)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.forward(2)
    timmy_the_turtle.left(25)

# Timmy_the_Turtle draws a Flower of Triangles.

for _ in range(120):
    timmy_the_turtle.color(random_color())
    for _ in range(4):  # draw square
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
    timmy_the_turtle.left(10)  # rotate








# Keeps the window open
screen = t.Screen()
screen.exitonclick()



