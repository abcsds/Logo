from turtle import *

mode('logo')
clearscreen()
speed(0)

def koch(size):
    if size > 10:
        koch(size*0.618)
        lt(60)
        koch(size*0.618)
        rt(120)
        koch(size*0.618)
        lt(60)
        koch(size*0.618)
    else:
        fd(size*0.618)
        lt(60)
        fd(size*0.618)
        rt(120)
        fd(size*0.618)
        lt(60)
        fd(size*0.618)

clearscreen()
lt(90)
pu()
fd(300)
pd()
rt(180)
speed(0)
koch(100)
