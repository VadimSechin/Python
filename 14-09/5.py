import turtle
import time

turtle.shape('turtle')
turtle.speed(10)

for i in range(1, 11):
    turtle.penup()
    turtle.goto(-i * 15, -i * 15)
    turtle.pendown()
    for k in range(4):
        turtle.forward(i * 30)
        turtle.left(90)
time.sleep(1)
