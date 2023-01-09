from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title('My Snake Game')
s.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

# Playing the game

game_is_on = True
# count = 0
# current = 0
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # Detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.increase()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    # Detect hitting wall
    for square in snake.snake[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            score.game_over()
            current += 1

    # if score.again() and current != count:
    #     game_is_on = True
    #     snake = Snake()
    #     food = Food()
    #     score = ScoreBoard()
    #     count += 1


s.exitonclick()
