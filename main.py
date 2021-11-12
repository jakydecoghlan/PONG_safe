from turtle import Turtle, Screen
from paleta import Paleta

screen = Screen()
screen.screensize(800, 600, "black")
screen.title("PONG")

paleta1 = Paleta()
paleta1.hideturtle()
paleta1.setposition(-650, 0)
paleta1.showturtle()

paleta2 = Paleta()
paleta2.hideturtle()
paleta2.setposition(650, 0)
paleta2.showturtle()

screen.listen()
screen.onkeypress(paleta1.up, "w")
screen.onkeypress(paleta1.down, "s")
screen.onkeypress(paleta2.up, "Up")
screen.onkeypress(paleta2.down, "Down")


screen.exitonclick()