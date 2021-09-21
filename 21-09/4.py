from random import *
import turtle
turtle.speed(10)
turtle.shape('turtle')
turtle.goto(600, 0)
turtle.goto(-600, 0)
x = -300
y = 0
ay = -10
Vx = 20
Vy = 40
dt = 0.1
for i in range(100000):
    turtle.goto(x, y)
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y <= 0:
        Vy = - Vy*0.7
        Vx = Vx*0.7
        y = 0
