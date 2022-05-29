from turtle import *

setup(800, 600)
bgcolor("Black")

pensize(1)
hideturtle()
pendown()
speed(100)

deg = 10

while deg <= 21 :
    pencolor("yellow")
    circle(30)
    right(deg)
    pencolor("red")
    circle(50)
    pencolor("#00cdfe")
    circle(70)
    pencolor("pink")
    circle(90)

    deg += 0.5

done()
