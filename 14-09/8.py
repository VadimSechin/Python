import time
import turtle

turtle.shape('turtle')
turtle.speed(10)

for i in range(36):
    turtle.forward(i * 5)
    turtle.left(90)
time.sleep(1)
