from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

