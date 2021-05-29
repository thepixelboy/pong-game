from turtle import Screen
from paddle import Paddle

# Setting up the screen
screen = Screen()
screen.title("Pong!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Variables
is_game_on = True

# Creating a paddle on screen
paddle = Paddle()

# Listening for a keypress to move the paddle
screen.listen()
screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")

while is_game_on:
  screen.update()



screen.exitonclick()