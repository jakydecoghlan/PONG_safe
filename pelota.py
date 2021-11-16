from turtle import Turtle
import random

# LEFT = (45, 135)
# RIGHT = (315, 225)



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed(2)
        

    def direction(self):
        direction = random.randint(0, 1)    # 0 para LEFT, 1 para RIGHT
        # LEFT = (45, 135)
        # RIGHT = (315, 225)
        if direction == 0:
            angle = random.randint(1, 180)
        elif direction == 1:
            angle = random.randint(180, 360)

        self.setheading(angle)
        

    def move(self):
        
        self.forward(20)
        
    def bounce(self):
        angle = self.heading()
        if self.xcor() > 0:
            self.setheading(180-angle)
        else:
            self.setheading(180-angle+360)




