import time
from random import randint
import turtle


number_of_turtles = 5
steps_of_time_number = 1000
turtles = []

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
t1 = pool[1]
t1.penup()
t1.goto(-200, -200)
t1.pendown()
t1.goto(-200, 200)
t1.goto(200, 200)
t1.goto(200, -200)
t1.goto(-200, -200)
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.right(randint(-180, 180))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(10)
        if unit.xcor() <= -200:
            unit.left(180-2*unit.heading())
        elif unit.xcor() >= 200:
            unit.left(180-2*unit.heading())
        elif unit.ycor() <= -200:
            unit.right(2 * unit.heading())
        elif unit.ycor() >= 200:
            unit.right(2 * unit.heading())

