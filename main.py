from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set screen environment
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PongGame")
screen.tracer(0)

# Declare objects for left and right paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

#Setup key listen
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.gp_up, "w")
screen.onkey(l_paddle.gp_down, "s")


game_is_on = True
