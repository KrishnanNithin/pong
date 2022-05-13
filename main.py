#imports
from turtle import Turtle, Screen
from paddle import Paddle

#Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

game_on = True

#initialize objects
lpaddle = Paddle((350, 0))
rpaddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(lpaddle.goup, "Up")
screen.onkeypress(lpaddle.godown, "Down")
screen.onkeypress(rpaddle.goup, "w")
screen.onkeypress(rpaddle.godown, "s")

while game_on:
    screen.update()

screen.exitonclick()