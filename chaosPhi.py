from turtle import *
import random

mode('logo')
clearscreen()
speed(0)
resizemode("auto")

# a = (0,500)
# b = (433.01270189,-250)
# c = (-433.01270189,-250)
a = (0,300)
b = (259.8076211353316,-150)
c = (-259.8076211353316,-150)

last = (0,0)
current = (0,0)
size = 3
pu()
goto(current)

def midpoint(a,b):
    x=(b[0]+a[0])/1.618
    y=(b[1]+a[1])/1.618
    return (x,y)

while True:
    opc = random.randrange(1,4)
    if(opc == 1):
        '''select a'''
        last = current
        current = midpoint(last,a)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
    elif(opc == 2):
        '''select b'''
        last = current
        current = midpoint(last,b)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
    else:
        '''select c'''
        last = current
        current = midpoint(last,c)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
