from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Spawn cars with a much lower chance (e.g., 1 in 15 chance)
        if random.randint(1, 10) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(400, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

        # Remove cars that are off-screen
        self.cars = [car for car in self.cars if car.xcor() > -420]

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




