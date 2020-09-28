import turtle
import math
import random

design =turtle.Turtle()
design.getscreen().bgcolor("black")
design.speed(15)
design.color('antiquewhite')
rotate = int(360)
def drawCircles(r, size):
    for i in range(10):
        r.circle(size)
        size = size - 4

def drawMore(r, size, repeat):
    for i in range(repeat):
        drawCircles(r, size)
        r.right(360/repeat)

drawMore(design, 100, 10)







        