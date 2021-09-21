import time
import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10)


def circle_l(r):
    for i in range(36):
        turtle.forward(r)
        turtle.left(10)


def circle_r(r):
    for i in range(36):
        turtle.forward(r)
        turtle.right(10)


turtle.right(90)
for i in range(6):
    circle_l(10 + i * 2)
    circle_r(10 + i * 2)
time.sleep(1)
turtle.reset()
