from turtle import Turtle, Screen
import time


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align='center', font=('arial', 24, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('arial', 56, 'normal'))
        # self.again()
    #
    # def again(self):
    #     s = Screen()
    #     user_bet = s.textinput(title='Play Again?', prompt='Do you want to play again (yes/no)?')
    #     return user_bet.lower()[0] == 'y'
