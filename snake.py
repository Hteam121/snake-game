from turtle import Turtle

MOVE_CONSTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake = []
        self.distance = 0

        for n in range(3):
            self.snake.append(Turtle(shape='square'))
            self.snake[len(self.snake) - 1].color('white')
            self.snake[len(self.snake) - 1].pensize(width=20)
            self.snake[len(self.snake) - 1].penup()
            self.snake[len(self.snake) - 1].backward(self.distance)
            self.distance += 20
        self.head = self.snake[0]

    def increase(self):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.pensize(width=20)
        snake.penup()
        snake.goto(self.snake[-1].position())
        self.snake.append(snake)

        self.distance += 20

    def move(self):
        for square in range(len(self.snake) - 1, 0, -1):
            x = self.snake[square - 1].xcor()
            y = self.snake[square - 1].ycor()
            self.snake[square].goto(x, y)
        self.snake[0].forward(MOVE_CONSTANT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
