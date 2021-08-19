import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_not_over = False
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=-70 + (turtle_index * 30))
    all_turtles.append(new_turtle)

if user_bet:
    race_not_over = True

while race_not_over:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_not_over = False
            if user_bet == turtle.pencolor():
                print("You Win!")
            else:
                print(f"You Lose. The {turtle.pencolor} turtle won.")
        r_dist = random.randint(0, 10)
        turtle.fd(r_dist)

screen.exitonclick()
