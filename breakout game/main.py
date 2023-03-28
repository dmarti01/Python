from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from brickz import Bricks
import time

screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle((0, -300))
bricks = Bricks()
bricks.create_bricks()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall Collision
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # top collision
    if ball.ycor() > 380:
        ball.bounce_y()

    # Paddle Collision
    if ball.distance(paddle) < 30 and ball.ycor() > -300:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False

    # Brick Collision
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scoreboard.point()

screen.exitonclick()