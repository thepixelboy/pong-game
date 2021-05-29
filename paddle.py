from turtle import Turtle

DEFAULT_MOVE = 20

class Paddle(Turtle):

  def __init__(self, position):
    super().__init__()
    self.position = position
    self.create_paddle()    

  def create_paddle(self):
    self.shape("square")
    self.color("white")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(self.position)

  def go_up(self):
    new_y_position = self.ycor() + DEFAULT_MOVE
    self.goto(self.xcor(), new_y_position)

  def go_down(self):
    new_y_position = self.ycor() - DEFAULT_MOVE
    self.goto(self.xcor(), new_y_position)