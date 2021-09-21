import time
import turtle

turtle.shape('turtle')
turtle.speed(10)

for i in range(500):
    r = i
    turtle.right(10)
    turtle.forward(0.05 * i)
time.sleep(1)
