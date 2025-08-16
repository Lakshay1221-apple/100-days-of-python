from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    #Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > -340:
        print("made contact")











screen.exitonclick()

