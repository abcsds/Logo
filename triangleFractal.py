from turtle import *

mode('logo')
clearscreen()
speed(0)

def triangle(size):
    if size > 10:
        lt(90)
        triangle(size*0.618)
        rt(135)
        triangle(size*sqrt(2)*0.618)
        lt(45)
        triangle(size*0.618)
    else:
        lt(90)
        fd(size)
        rt(135)
        fd(size*sqrt(2))
        lt(45)
        fd(size)

clearscreen()
lt(90)
pu()
fd(400)
pd()
rt(180)
speed(0)
triangle(50)
