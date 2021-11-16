from turtle import Screen
from paleta import Paleta
from pelota import Ball



screen = Screen()
screen.screensize(800, 600, "black")
screen.title("PONG")
screen.mode("logo")


paleta1 = Paleta()
paleta1.hideturtle()
paleta1.setposition(-650, 0)
paleta1.showturtle()

paleta2 = Paleta()
paleta2.hideturtle()
paleta2.setposition(650, 0)
paleta2.showturtle()

ball = Ball()




screen.listen()
screen.onkeypress(paleta1.up, "w")
screen.onkeypress(paleta1.down, "s")
screen.onkeypress(paleta2.up, "Up")
screen.onkeypress(paleta2.down, "Down")

# screen.onkeyrelease(paleta1.stop, "w")
# screen.onkeyrelease(paleta1.stop, "s")
# screen.onkeyrelease(paleta2.stop, "Up")
# screen.onkeyrelease(paleta2.stop, "Down")

game_is_on = True
while game_is_on:
    ball.direction()
    direction = ball.heading()
    pelota_en_juego = True
    while pelota_en_juego:
        ball.move()
        if ball.ycor() > 200 or ball.ycor() < -200:
            screen.tracer(0)
            ball.bounce()
            screen.tracer(1)


screen.exitonclick()