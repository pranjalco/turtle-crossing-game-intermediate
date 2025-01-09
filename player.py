from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.create_turtle()

    def create_turtle(self):
        """It will create turtle."""
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        x = self.xcor()
        self.goto(x, new_y)

    def reset_turtle_position(self):
        self.goto(STARTING_POSITION)

