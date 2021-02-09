from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle Instances
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# Ball Instances
ball = Ball()

# Scoreboard Instance
scoreboard = Scoreboard()


# Screen Listeners
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

# Game Logic
game_is_on = True
while game_is_on:
    time.sleep(0.025)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50)  :
        print("MADE CONTACT")
        ball.bounce_x()

    #  Left player point
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #  Right player point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()