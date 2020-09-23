import turtle
        
def draw_tree(turt, width, height):
    draw_trunk(turt, width, height)
    draw_leafs(turt, width, height)

def draw_trunk(turt, width, height):
    turt.color('brown')
    turt.begin_fill()
    turt.setheading(0)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.right(90)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.end_fill()

def draw_leafs(turt, width, height, traingles=3):
    turt.color('green')
    for i in range(traingles):
        draw_traingle(turt, width,height)
        height_increase = height/2
        turt.sety(turt.ycor()+ height_increase)

def draw_traingle(turt, width, height):
    branch_overhang = height
    traingle_height = 2*height

    turt.begin_fill()

    x_init, y_init = (turt.xcor(), turt.ycor())
    x_middle = x_init + width/2.0
    x_bottom_left = x_init - branch_overhang
    x_bottom_right = x_init + width + branch_overhang
    y_top = y_init + traingle_height

    turt.goto(x_bottom_left, y_init)
    turt.goto(x_middle, y_top)
    turt.goto(x_bottom_right, y_init)
    turt.goto(x_init, y_init)

    turt.end_fill()
    
width= 50
height= 100
  
turt = turtle.Turtle()
draw_trunk(turt, width , height)
draw_leafs(turt, width, height)
turtle.done()

