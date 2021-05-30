from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Setting up the screen
screen = Screen()
screen.title("Pong!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Variables
is_game_on = True

# Creating the paddles on the screen
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Listening for a keypress to move the paddle
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while is_game_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  # Detect collision with the wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    # the ball bounces on the ceilling or on the floor
    ball.bounce()

screen.exitonclick()