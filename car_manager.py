from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE = "square"
STRETCH_LEN = 2
LEFT = 180
X_SPAWN = 300
Y_RANGE = 250


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle(shape=SHAPE)
        car.penup()
        car.setheading(LEFT)
        car.turtlesize(stretch_len=STRETCH_LEN)
        car.color(random.choice(COLORS))
        y_spawn = random.randint(-Y_RANGE, Y_RANGE)
        car.goto(X_SPAWN, y_spawn)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

