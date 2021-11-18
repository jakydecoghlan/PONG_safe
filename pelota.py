from turtle import Turtle
import random


# LEFT = (45, 135)
# RIGHT = (315, 225)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")


    def direction(self):
        direction = random.randint(0, 1)  # 0 = LEFT, 1 = RIGHT
        # LEFT = (315, 225)
        # RIGHT = (45, 135)
        if direction == 0:
            angle = random.randint(225, 315)
        elif direction == 1:
            angle = random.randint(45, 135)
        self.setheading(angle)

    def move(self):
        self.forward(20)

    def bounce_y(self):
        angle = self.heading()
        if self.xcor() > 0:
            self.setheading(180 - angle)
        else:
            self.setheading(180 - angle + 360)

    def bounce_x(self):
        angle = self.heading()
        self.setheading(360 - angle)

    def goal(self):
        if self.xcor() > 0:
            angle = random.randint(225, 315)
            self.setheading(angle)
        elif self.xcor() < 0:
            angle = random.randint(45, 135)
            self.setheading(angle)
        self.goto(0, 0)




