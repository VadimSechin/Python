import time
import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10)


def mnogougolnik(n, r):
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    turtle.left(180 / n)
    for k in range(n):
        turtle.forward(2 * r * np.sin(2 * np.pi / 2 / n))
        turtle.left(360 / n)
    turtle.right(180 / n)


def circle_l(r):
    for i in range(36):
        turtle.forward(r)
        turtle.left(10)


def circle_r(r):
    for i in range(36):
        turtle.forward(r)
        turtle.right(10)


for i in range(4):
    circle_l(10)
    circle_r(10)
    turtle.right(180 / 4)
time.sleep(1)
turtle.reset()
