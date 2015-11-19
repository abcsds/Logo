from turtle import *

mode('logo')
clearscreen()

def constant(size):
    speed(0)
    while True:
        fd(size)
        rt(137.5)
        size +=1

def linear(size):
    speed(0)
    while True:
        fd(size)
        rt(137.5)
        size *=1.101

def linearDots(size):
    pu()
    speed(0)
    while True:
        dot()
        fd(size)
        rt(137.5)
        size *=1.101

def constantDots(size):
    pu()
    speed(0)
    while True:
        dot()
        fd(size)
        rt(137.5)
        size +=1

def increasingAngle(size):
    speed(0)
    while True:
        fd(size)
        rt(size*1.618)
        size +=1

def increasingAngleLin(size):
    speed(0)
    while True:
        fd(size)
        rt(360/size)
        size +=1
