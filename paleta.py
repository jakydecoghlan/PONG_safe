from turtle import Turtle

UP = 0
DOWN = 180

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
        self.forward(20)

    def down(self):
        self.forward(-20)







