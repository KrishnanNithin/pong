from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.scoreL = 0
        self.scoreR = 0
        self.update()
    
    def update(self):
        self.clear()
        self.write(f'{self.scoreL}: {self.scoreR}', align='center', font=('Arial', 20, 'normal'))
