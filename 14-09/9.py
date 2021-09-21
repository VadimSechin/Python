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


turtle.left(90)
for i in range(3, 10):
    r = 15 * (i - 2)
    mnogougolnik(i, r)
time.sleep(1)
turtle.reset()
