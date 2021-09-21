import time
import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10)


def duga1():
    for i in range(18):
        turtle.left(10)
        turtle.forward(10)


turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(45, 120)
turtle.pendown()
turtle.color("black", "blue")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.goto(-45, 120)
turtle.pendown()
turtle.color("black", "blue")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 120)
turtle.right(90)
turtle.pendown()
turtle.pensize(10)
turtle.color("black", "black")
turtle.forward(60)
turtle.penup()
turtle.goto(-180 / np.pi, 80)
turtle.pendown()
turtle.pensize(10)
turtle.color("red", "red")
duga1()
time.sleep(1)
