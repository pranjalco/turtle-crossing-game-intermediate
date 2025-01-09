from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level_number = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level()

    def level(self):
        self.goto(-220, 260)
        self.write(f"Level: {self.level_number}", align="center", font=("Courier", 18, "normal"))

    def update_level(self):
        self.clear()
        self.level_number += 1
        self.level()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
