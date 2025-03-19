import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""
# Turtle Crossing Game
A fun game where the player guides a turtle to the top while avoiding moving cars. The game gets harder as car speeds increase with each level.  

## Screenshots
![ss1](./screenshots/1.PNG), ![ss2](./screenshots/2.PNG), ![ss3](./screenshots/3.PNG)

## Author
Pranjal Sarnaik

## Features
- Move the turtle using `w` (up) and `s` (down).  
- Avoid cars moving from right to left.  
- Reach the top to advance to the next level.  
- Car speed increases as levels progress.  
- Game over on collision with a car.  

## Level
Intermediate

## Tech Stack
Python | Turtle | OOP | Random Module | Game Logic | Game Development

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/turtle-crossing-game-intermediate.git

3. Run:
    ```bash  
   python app.py
"""

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing by Pranjal Sarnaik")
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")

counter = 0
time_car_generate = 5

game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()

    # Generating cars at specific intervals
    if counter > time_car_generate:
        car.create_car()
        counter = 0

    car.move()

    # Detect if turtle wins
    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset_turtle_position()
        car.increase_car_speed()

    # Checking collision with car
    for c in car.cars:
        if player.distance(c) < 25:
            scoreboard.game_over()
            game_is_on = False
            print("Game Over")

screen.exitonclick()
