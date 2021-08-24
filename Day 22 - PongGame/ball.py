from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_dir = 1
        self.y_dir = 1
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_dir * 10, self.ycor() + self.y_dir * 10)

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
