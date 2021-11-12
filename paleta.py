from turtle import Turtle

UP = 90
DOWN = 270

class Paleta(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5, 5)
        self.speed("fastest")
        self.setheading(UP)

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)


