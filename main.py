import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.onkey(player.up, "Up")

car_manager = CarManager()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        score.increase_level()

screen.exitonclick()