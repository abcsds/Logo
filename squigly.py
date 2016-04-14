from turtle import *

mode('logo')
clearscreen()
speed(0)

n = 4
divisor = .5
side = 50
minSize = side/(divisor*n)

def koch(size):
    if size > minSize:
        koch(size*divisor)
        lt(90)
        koch(size*divisor)
        rt(90)
        koch(size*divisor*sqrt(2))
        lt(45)
        koch(size*divisor)
    else:
        fd(size)
        lt(90)
        fd(size)
        rt(135)
        fd(size*sqrt(2))
        lt(45)
        fd(size)

clearscreen()
lt(90)
pu()
fd(300)
pd()
rt(180)
speed(0)
koch(50)
