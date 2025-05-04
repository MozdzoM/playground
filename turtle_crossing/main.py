import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from street import Street

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray10")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
street = Street()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create moving cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player crossed
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.speed_up()

screen.exitonclick()
