


# THE TURTLE RACE GAME with Betting Feature


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
                break  # Stop race

screen.exitonclick()