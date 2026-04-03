from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Scorecount

# Your turtle code here
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my Snake game Play")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scorecount()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreUpdate()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False 
        score.gameover()

    for seg in snake.sagments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False 
            score.gameover()






screen.exitonclick()
