import turtle

c=turtle.Turtle()
c.getscreen().bgcolor("black")
c.color("red","yellow")
c.speed(15)
c.begin_fill()
c.setheading(0)
for i in range(500):
    c.forward(300)
    c.right(170)
turtle.done()
