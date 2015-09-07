from turtle import *

mode('logo')
clearscreen()

speed(0)
def ftree(size):
  if size >= 5:
    lt(180/2)
    fd(size)
    ftree(size/1.5)
    bk(size)
    rt(180)
    fd(size)
    ftree(size/1.5)
    bk(size)
    lt(180/2)

size = 200
ftree(size)
