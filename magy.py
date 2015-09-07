from turtle import *

def tree(size):
  if size >= 20:
    fd(size)
    lt(137.5/2)
    tree(size/1.618)
    rt(137.5/2)
    tree(size/1.618)
    rt(137.5/2)
    tree(size/1.618)
    lt(137.5/2)
    bk(size)

lt(90)
bk(300)
tree(300)
