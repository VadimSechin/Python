import turtle
import time

turtle.shape('turtle')
turtle.speed(10)

n = 12
for i in range(n):
    turtle.right(360 / n)
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180)
time.sleep(1)
