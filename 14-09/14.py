import time
import turtle

turtle.shape('turtle')
turtle.speed(10)


def star(n):
    for i in range(n):
        turtle.forward(200)
        turtle.right(180 - 360 / n / 2)


star(5)
time.sleep(1)
turtle.reset()

star(11)
time.sleep(1)
turtle.reset()
