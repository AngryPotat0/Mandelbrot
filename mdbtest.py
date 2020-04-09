import turtle
from math import *
turtle.setup(640,480)
turtle.colormode(255)
t = turtle.Pen()
turtle.bgcolor("white")
t.ht()
t.speed(0)
turtle.tracer(0,0)

color1 = [1, 11, 74]
color2 = [255, 255, 255]
colorMap = [[0 for i in range(3)] for j in range(100)]
for i in range(100):
   for j in range(3):
       colorMap[i][j] = color1[j] + (color2[j] - color1[j]) * i / 100

t.penup()
t.goto(-320,240)
t.setheading(0)

for h in range(-240, 240):
    for w in range(-320, 320):
        x = (w - 100) / 180
        y = h / 180
        c = x + y * 1j
        z = 0
        for i in range(1, 100):
            z = z * z + c
            if abs(z) > 10.0:
                break
        if i >= 99:
            t.pencolor(0, 0, 0)
        else:
            t.pencolor(floor(colorMap[i][0]), floor(colorMap[i][1]), floor(colorMap[i][2]))
        t.forward(1)
    t.penup()
    t.backward(640)
    t.right(90)
    t.forward(1)
    t.left(90)
    t.pendown()

turtle.update()
turtle.done()
