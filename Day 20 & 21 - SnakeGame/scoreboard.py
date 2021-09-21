from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pu()
        self.hideturtle()
        self.color('white')
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.print_score()

