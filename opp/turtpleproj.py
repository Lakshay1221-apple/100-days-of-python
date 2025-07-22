from turtle import Turtle, Screen
import random



# import turtle as t

timmy_the_turtle = Turtle()
# tom_the_turtle = Turtle()

# tom_the_turtle.shape("turtle")
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# tom_the_turtle.left(180)

# for _ in range(15):
#     tom_the_turtle.forward(10)
#     tom_the_turtle.penup()
#     tom_the_turtle.forward(10)
#     tom_the_turtle.pendown()
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for _ in range(1000):
    timmy_the_turtle.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink"]))
    timmy_the_turtle.forward(25)
    timmy_the_turtle.setheading(random.choice(directions))





screen = Screen()
screen.exitonclick()




