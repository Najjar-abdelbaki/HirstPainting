# import colorgram
# colors = colorgram.extract("hist.jpg", 10)
#
# colours=[]
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     colours.append(new_color)
#
# print(colours)

import  turtle as t
import random


colors = [(225, 230, 236), (222, 234, 230), (235, 227, 210), (58, 105, 145), (130, 91, 61), (221, 201, 114), (218, 153, 76), (237, 225, 234), (146, 177, 199), (193, 144, 170)]

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)


for i in range(1, 101):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = t.Screen()
screen.exitonclick()