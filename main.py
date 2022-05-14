#imports
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

game_on = True

#initialize objects
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(rpaddle.goup, "Up")
screen.onkeypress(rpaddle.godown, "Down")
screen.onkeypress(lpaddle.goup, "w")
screen.onkeypress(lpaddle.godown, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce()

    #detect collision with paddles
    if (ball.xcor()>315) and (ball.distance(rpaddle)<60):
        ball.deflect()
        ball.move_speed *= 0.9
    if (ball.xcor()<-315) and (ball.distance(lpaddle)<60):
        ball.deflect()
        ball.move_speed *= 0.9

    #detect ball out of bounds
    if ball.xcor() > 350:
        ball.move_speed = 0.1
        ball.respawn()
        scoreboard.scoreL += 1
        scoreboard.update()
    
    if ball.xcor() < -350:
        ball.move_speed = 0.1
        ball.respawn()
        scoreboard.scoreR += 1
        scoreboard.update()


screen.exitonclick()