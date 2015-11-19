from turtle import *
import random

mode('logo')
clearscreen()
speed(0)
resizemode("auto")

# hexagon
a = (0,300)
b = (260,150)
c = (260,-150)
d = (0,-300)
e = (-260,-150)

last = (0,0)
current = (0,0)
size = 4
pu()
goto(current)

def midpoint(a,b):
    x=(b[0]+a[0])/2
    y=(b[1]+a[1])/2
    return (x,y)

while True:
    opc = random.randrange(1,7)
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
    elif(opc == 3):
        '''select c'''
        last = current
        current = midpoint(last,c)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
    elif(opc == 4):
        '''select d'''
        last = current
        current = midpoint(last,d)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
    elif(opc == 5):
        '''select e'''
        last = current
        current = midpoint(last,e)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
    else:
        '''select f'''
        last = current
        current = midpoint(last,f)
        goto(current)
        pd()
        begin_fill()
        circle(size)
        end_fill()
        pu()
