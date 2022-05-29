from turtle import *

colors = ['red', 'yellow', 'pink', '#00cdfe']
setup(800, 600)
bgcolor("Black")

pensize(1)
hideturtle()
pendown()
speed(100)

deg = 10
deg2=50
rad=30

for i in range(deg2) :
    pencolor(colors[i%4])
    circle(rad)
    right(deg)

    rad+=2
    deg += 0.5

done()
