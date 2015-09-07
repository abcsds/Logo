from turtle import *

mode('logo')
clearscreen()
speed(0)

def lump(size):
    if size > 10:
        lt(90)
        lump(size*0.618)
        rt(45)
        lump(size*.25*0.618)
        rt(45)
        lump(size*0.618)
        rt(45)
        lump(size*.25*0.618)
        rt(45)
        lump(size*0.618)
        lt(90)
    else:
        lt(90)
        fd(size*0.618)
        rt(45)
        fd(size*.25*0.618)
        rt(45)
        fd(size*0.618)
        rt(45)
        fd(size*.25*0.618)
        rt(45)
        fd(size*0.618)
        lt(90)

clearscreen()
rt(180)
speed(0)
lump(200)
