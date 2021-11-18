from turtle import Screen
from paleta import Paleta
from pelota import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.screensize(800, 600, "black")
screen.title("PONG")
screen.mode("logo")

screen.tracer(0)
scoreboard = Scoreboard()
screen.tracer(1)

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

game_is_on = True
while game_is_on:
    screen.tracer(0)
    ball.direction()
    screen.tracer(1)
    # direction = ball.heading()
    pelota_en_juego = True
    while pelota_en_juego:
        ball.move()
        if ball.ycor() > 500 or ball.ycor() < -500:
            screen.tracer(0)
            ball.bounce_y()
            screen.tracer(1)
        if ball.distance(paleta2) < 50 and ball.xcor() > 620 or ball.distance(paleta1) < 50 and ball.xcor() < -620:
            screen.tracer(0)
            ball.bounce_x()
            screen.tracer(1)
        #  detectar gol paleta 1
        if ball.xcor() > 780:
            screen.tracer(0)
            ball.goal()
            scoreboard.l_point()
            screen.tracer(1)

        # detectar gol paleta 2
        if ball.xcor() < -780:
            screen.tracer(0)
            ball.goal()
            scoreboard.r_point()
            screen.tracer(1)

screen.exitonclick()