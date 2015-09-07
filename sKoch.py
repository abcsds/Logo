from turtle import *

mode('logo')
clearscreen()
speed(0)

def koch(size):
    if size > 5:
        koch(size*0.618)
        lt(90)
        koch(size*0.618)
        rt(90)
        koch(size*0.618)
        rt(90)
        koch(size*0.618)
        lt(90)
        koch(size*0.618)
    else:
        fd(size*0.618)
        lt(90)
        fd(size*0.618)
        rt(90)
        fd(size*0.618)
        rt(90)
        fd(size*0.618)
        lt(90)
        fd(size*0.618)

clearscreen()
lt(90)
pu()
fd(300)
rt(90)
bk(200)
pd()
rt(90)
speed(0)
koch(50)
