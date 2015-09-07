from turtle import *

mode('logo')
clearscreen()

speed(0)
def tree(size):
  if size >= 10:
    fd(size)
    lt(137.5/2)
    tree(size/1.618)
    rt(137.5)
    tree(size/1.618)
    lt(137.5/2)
    bk(size)

size = 200
for i in range(6):
    tree(size)
    size=size*0.618
    rt(60)
