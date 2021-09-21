import time
import turtle

turtle.shape('turtle')


def duga1():
    for i in range(18):
        turtle.forward(10)
        turtle.left(10)
    turtle.forward(10)


def duga2():
    for i in range(18):
        turtle.forward(2)
        turtle.left(10)
    turtle.forward(2)


turtle.right(90)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
for i in range(6):
    duga1()
    duga2()
time.sleep(1)
