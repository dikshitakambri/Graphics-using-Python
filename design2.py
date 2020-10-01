import turtle
import math
import random

window = turtle.Screen()
window.bgcolor("black")

design =turtle.Turtle()
design.speed(20)
design.color('chartreuse')
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

design2 =turtle.Turtle()
design2.speed(20)
design2.color('red')
rotate = int(270)
def drawCircles(r, size):
    for i in range(4):
        r.circle(size)
        size = size - 10

def drawMore(r, size, repeat):
    for i in range(repeat):
        drawCircles(r, size)
        r.right(360/repeat)

drawMore(design2, 100, 10)

design3 =turtle.Turtle()
design3.speed(20)
design3.color('darkorchid')
rotate = int(180)
def drawCircles(r, size):
    for i in range(10):
        r.circle(size)
        size = size - 15

def drawMore(r, size, repeat):
    for i in range(repeat):
        drawCircles(r, size)
        r.right(360/repeat)

drawMore(design3, 100, 10)

design4 =turtle.Turtle()
design4.speed(20)
design4.color('deepskyblue')
rotate = int(90)
def drawCircles(r, size):
    for i in range(4):
        r.circle(size)
        size = size - 19

def drawMore(r, size, repeat):
    for i in range(repeat):
        drawCircles(r, size)
        r.right(360/repeat)

drawMore(design4, 100, 10)





        