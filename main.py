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

# Creating the paddles on the screen
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Listening for a keypress to move the paddle
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while is_game_on:
  screen.update()



screen.exitonclick()