from turtle import *

speed(0)
hideturtle()
setup(1100,600)
bgcolor("white")
pencolor("#0d77b5")
pensize(15)

penup()

goto(-300, 100)
pendown()

speed(5)
right(90)

# I
def line():
    forward(200)
line()

penup()
left(90)

pendown()

penup()

# N
goto(-250, -100)
left(90)
pendown()

forward(150)
penup()
goto(-250, 10)

pendown()

circle(-40,180)
forward(107)
penup()

# F

goto(-130, -100)
left(180)
pendown()
forward(150)
circle(-50,110)
penup()

goto(-130,40)

left(200)

pendown()
forward(15)
penup()
right(180)

pendown()
forward(130)

# O

circle(-72)

penup()

#S

goto(80,-80)
right(90)
pendown()

circle(40,230)
forward(70)
circle(-40,200)

# Y

forward(130)
right(55)
forward(80)
left(180)
forward(190)

penup()

# S

goto(342, 10)
pendown()


circle(40,245)

forward(80)
circle(-40,220)

penup()

# circle

goto(390,120)

pensize(3)
pendown()
circle(20)

penup()

# circle R

goto(365,107)

pendown()
pensize(4)
forward(25)

right(90)
circle(-8,180)

penup()
for i in range(5):
    backward(1)

left(180)
pendown()

right(45)

forward(10)
hideturtle()

penup()

done()