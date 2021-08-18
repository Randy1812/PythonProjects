import random
from turtle import Turtle, Screen

# rgb_colors = []
# colors = colorgram.extract("hirst.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_col = (r, g, b)
#     rgb_colors.append(new_col)
# print(rgb_colors)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

t = Turtle()
t.speed('fastest')
t.ht()
screen = Screen()
screen.colormode(255)

# print(t.xcor())
# print(t.ycor())
t.pu()
t.width(20)
t.goto(-250, -250)

# for i in range(10):
#     for j in range(10):
#         t.color(random.choice(color_list))
#         t.fd(1)
#         t.pu()
#         t.fd(50)
#         t.pd()
#     t.pu()
#     t.lt(180)
#     t.fd(510)
#     t.rt(90)
#     t.fd(50)
#     t.rt(90)
#     t.pd()

for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(color_list))
        t.fd(50)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(500)
    t.rt(180)

screen.exitonclick()