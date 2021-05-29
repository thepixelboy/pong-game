from turtle import Turtle

PADDLE_POSITION = (350, 0)
DEFAULT_MOVE = 20

class Paddle:

  def __init__(self):
    self.create_paddle()

  def create_paddle(self):
    self.paddle = Turtle(shape="square")
    self.paddle.color("white")
    self.paddle.penup()
    self.paddle.shapesize(stretch_wid=5, stretch_len=1)
    self.paddle.goto(PADDLE_POSITION)

  def go_up(self):
    new_y_position = self.paddle.ycor() + DEFAULT_MOVE
    self.paddle.goto(self.paddle.xcor(), new_y_position)

  def go_down(self):
    new_y_position = self.paddle.ycor() - DEFAULT_MOVE
    self.paddle.goto(self.paddle.xcor(), new_y_position)