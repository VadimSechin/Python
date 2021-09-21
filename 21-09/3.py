import turtle
import time


L = []
s = open('rules.txt', 'r')
s = s.readlines()
for j in s:
    L.append(eval(j.strip()))


def write(n):
    turtle.speed(10)
    turtle.shape('turtle')
    try:
        numbers = str(n)
        for num in numbers:
            n = int(num)
            for i in L[n]:
                if i[2] == 1:
                    turtle.pendown()
                if i[2] == 0:
                    turtle.penup()
                turtle.forward(i[0])
                turtle.right(i[1])
            turtle.penup()
            turtle.forward(15)
            turtle.pendown()
    except:
        print('Это не число')

input = input()
write(input)

time.sleep(1)