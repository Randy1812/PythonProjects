from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color('white')
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
