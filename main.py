import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_timer % 6 == 0:
        car_manager.create_car()
    if car_manager.cars:
        car_manager.move_cars()

    # Detect collision with finish line
    if player.in_goal():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.update_score()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    game_timer += 1

screen.exitonclick()
