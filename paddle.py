from gzip import _PaddedFile
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.setposition(position)
    
    def goup(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def godown(self):
        self.goto(self.xcor(), self.ycor()-20)