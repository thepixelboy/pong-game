from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.title("Pong!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Variables
is_game_on = True

# Functions
def exit_game():
  globals()["is_game_on"] = False

# Creating the paddles, ball and scoreboard on the screen
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listening for a keypress to move the paddle
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(exit_game, "q")

while is_game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect collision with the wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    # the ball bounces on the ceilling or on the floor
    ball.bounce_y()

  # Detect collision with paddle
  if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
    ball.bounce_x()

  # Detect r_paddle misses
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.reset_position()
  
  # Detect l_maddle misses
  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.reset_position()

screen.exitonclick()