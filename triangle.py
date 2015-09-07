from turtle import *

mode('logo')
clearscreen()
speed(0)

side = 20
maxSize = side/(1.618*2)

def koch(size):
    if size > maxSize:
        koch(size*0.618)
        lt(60)
        koch(size*0.618)
        rt(120)
        koch(size*0.618)
        lt(60)
        koch(size*0.618)
    else:
        fd(size)
        lt(60)
        fd(size)
        rt(120)
        fd(size)
        lt(60)
        fd(size)

clearscreen()
lt(90)
pu()
fd(300)
pd()
rt(180)
speed(0)
for i in range(3):
    koch(side)
    rt(120)
