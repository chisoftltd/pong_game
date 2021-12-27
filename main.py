from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

#   Set screen environment
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1100, height=800)
screen.title("PongGame")
screen.tracer(0)

#   Declare objects for left and right paddles
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()

#   Setup key listen
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #   Detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    #   Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()

    #   Detect R paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        score.l_point()

    #   Detect L paddle misses
    if ball.xcor() < -360:
        ball.reset_position()
        score.r_point()
screen.exitonclick()