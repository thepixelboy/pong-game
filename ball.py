from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.create_ball()

  def create_ball(self):
    self.shape("square")
    self.color("white")
    self.penup()
    self.x_move = 10
    self.y_move = 10

  def move(self):
    new_x_position = self.xcor() + self.x_move
    new_y_position = self.ycor() + self.y_move
    self.goto(new_x_position, new_y_position)

  def bounce(self):
    self.y_move *= -1