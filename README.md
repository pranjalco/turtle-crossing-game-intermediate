# Project 17: Turtle Crossing Game

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 21 Dec 2024

## Description
A fun and interactive game where the player guides a turtle from the bottom to the top of the screen while avoiding cars moving from right to left. The game becomes progressively challenging as the cars move faster with each level. The player uses `w` to move the turtle up and `s` to move it down. The game ends if the turtle collides with a car.

## How to Use
1. Use the `w` key to move the turtle upward.
2. Use the `s` key to move the turtle downward.
3. Avoid colliding with the cars moving from right to left.
4. Reach the top of the screen to complete the level and reset the turtle’s position.
5. Progress through levels as the car speed increases.
6. The game ends if the turtle collides with a car.

## Level
- **Level**: Intermediate
- **Skills**: Object-Oriented Programming (OOP), Python Turtle Module, Time Module, Random Module, Game Development.
- **Domain**: Game Development

## Features
- **Player**:  
  - The player can move the turtle up and down using the `w` and `s` keys.
  - The turtle's position resets upon completing a level.
  - The car speed increases with each level.

- **CarManager**:  
  - Generates cars with random colors ("red", "orange", "yellow", "green", "blue", "purple").
  - Cars are created at random positions along the y-axis and move from right to left.
  - Car speed increases as levels progress.

- **Scoreboard**:  
  - Displays the current level of the game.
  - Updates the level upon successful completion.
  - Displays "Game Over" when the player loses.


## Folder Structure
- **experiments**: Contains temporary files and practice code used during development.
- **screenshots**: Includes gameplay screenshots.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/turtle-crossing-game-intermediate.git
   ```

2. Navigate to the project directory:
   ```bash
   cd turtle-crossing-game-intermediate
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

---

**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*