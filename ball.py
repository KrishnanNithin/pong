from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    
    def bounce(self):
        self.y_move *= -1

    def deflect(self):
        self.x_move *= -1