import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_POSITIONS = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.cars = []

    def create_car(self):

        y_position = random.choice(CAR_POSITIONS)
        c = Turtle()
        c.penup()
        c.speed(0)
        c.shape("square")
        c.shapesize(stretch_wid=1, stretch_len=2)
        c.color(random.choice(COLORS))
        c.goto(300, y_position)
        self.cars.append(c)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT


