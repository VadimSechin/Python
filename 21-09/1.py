from random import *
import turtle
turtle.speed(10)
turtle.shape('turtle')
for i in range(100):
    turtle.forward(randint(0, 20))
    turtle.right(randint(-360, 360))
