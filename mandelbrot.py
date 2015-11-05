from turtle import *

mode('logo')
clearscreen()
speed(0)
size = 4     # size of dots
scaler = 300 # how much to zoom in
screen = 400 # screen of sight in fractal
depth = 100   # recursion for f(z)
res = 5      # how many pixels to jump for next recursion


# current = [-200, 200]
pu()

for a in range(-screen,screen,res):
    for b in range(-screen,screen,res):
        old = 0
        new = 0
        # Does it diverge?
        flag = False
        for z in range(depth):
            old = new
            new = (old)**2 + (a/scaler)+((b/scaler)*1j)
            if abs(new) >= 2: # diverges
                flag = True
                break
        pu()
        goto((a,b))
        if flag:
            pd()
            begin_fill()
            circle(size)
            end_fill()
pu()
while True:
    goto((0,0))
