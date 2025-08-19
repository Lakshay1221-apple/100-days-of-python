from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player
import time

# You need to import the constant from player.py to use it here.
from player import FINISH_LINE_Y

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

# Create game objects
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

# Key bindings
screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")

# Game variables
game_is_on = True

# Main loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Always try to create cars (randomness handled inside CarManager)
    car_manager.create_car()
    car_manager.move_cars()

    # Collision detection
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Win condition (player reaches finish line)
    if player.ycor() > FINISH_LINE_Y:  # Using the constant now
        player.goto(0, -250)  # reset position
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

