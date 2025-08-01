# #In this code, we create a turtle graphics program that allows the user to control a turtle using keyboard inputs.
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# tim.speed("fastest")
# tim.color("blue")
# tim.shape("turtle")
#
# def move_up():
#     tim.setheading(90)
#     tim.forward(10)
#
#
# def move_down():
#     tim.setheading(270)
#     tim.forward(10)
#
#
# def move_left():
#     tim.setheading(180)
#     tim.forward(10)
#
#
# def move_right():
#     tim.setheading(0)
#     tim.forward(10)
#
# def draw_square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
# def pen_up():
#     tim.penup()
#
# def pen_down():
#     tim.pendown()
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def draw_circle():
#     tim.circle(50)
#
# def draw_anti_circle():
#     tim.circle(-50)
#
# screen.listen()
# screen.onkey(move_up, " Up")
# screen.onkey(move_down, "Down")
# screen.onkey(move_left, "Left")
# screen.onkey(move_right, "Right")
# screen.onkey(draw_square, "S")
# screen.onkey(pen_up, "U")
# screen.onkey(pen_down, "D")
# screen.onkey(clear_screen, "C")
# screen.onkey(draw_circle, "O")
# screen.onkey(draw_anti_circle, "A")
#
# screen.mainloop()



# THE TURTLE RACE GAME

from turtle import Turtle, Screen
import random

# Create turtles
colors = ["red", "blue", "green", "yellow"]
turtles = []

screen = Screen()
screen.setup(width=800, height=400)  # Make enough space

# Get user bet once before race starts
bet = screen.textinput("Make your bet", "Which turtle will win? (red/blue/green/yellow)").lower()

if bet not in colors:
    print("Invalid bet. Please choose from red, blue, green, or yellow.")
    screen.bye()
else:
    # Create turtles dynamically
    for i in range(4):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(-350, 100 - i * 50)  # Start line positions
        t.speed("fastest")
        turtles.append(t)

    race_on = True

    while race_on:
        for turtle in turtles:
            # Move each turtle a small random step
            turtle.forward(random.randint(5, 15))

            # Check if turtle crosses finish line
            if turtle.xcor() > 350:
                winner = turtle.color()[0]  # Get winning turtle color
                screen.title(f"{winner.capitalize()} turtle won the race!")
                print(f"🏁 Winner: {winner.capitalize()}")

                # Compare winner with user bet
                if bet == winner:
                    print(f"🎉 You guessed it! The {bet} turtle won!")
                else:
                    print(f"❌ Sorry! You picked {bet}, but {winner} won.")

                race_on = False
                print("Thank you for playing!")
                print("Exiting")

                break  # Stop race

screen.exitonclick()

