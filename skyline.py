import turtle

turtle.setup(500,500)


draw = turtle.Turtle()
 
"""
x = int(input("Enter the x-value: "))

y = int(input("Enter the y-value: "))

width = int(input("Enter the width: "))

height = int(input("Enter the height: "))

size = int(input("Enter the size: "))

color = input("Enter a color: ")
""" 

def draw_rectangle(draw,x,y,width,height,size,color):
    draw.fillcolor(color)
    draw.pencolor(color)
    draw.begin_fill()
    draw.pensize(size)
    draw.setheading(0)
 
    draw.up()
    draw.goto(x,y)
    draw.down()
  
    draw.forward(width)

    draw.right(90)
    draw.forward(height)

    draw.right(90)
    draw.forward(width)

    draw.right(90)
    draw.forward(height)
    draw.end_fill()

def draw_triangle(draw,x,y,height,width,size, color):

    draw.fillcolor(color)
    draw.pencolor(color)
    draw.begin_fill()

    draw.setheading(0)
 
   

    draw.pensize(size)

    draw.goto(x,y)

 
    draw.right(height)
    draw.forward(width)
 
    draw.right(height)
    draw.forward(width)
    draw.end_fill()

def draw_circle(draw,width,color):

    draw.fillcolor(color)
    draw.pencolor(color)
    draw.begin_fill()

    draw.goto(x,y)

    draw.pensize(size)

    draw.circle(width)

    draw.end_fill()


def turtle_state():

    turtle.isdown()

    turtle.heading()

    turtle.xcor()

    turtle.ycor()

def first_skyline():
    

    draw.fillcolor("wheat")
    draw.pencolor("wheat")
    draw.begin_fill()

    draw.forward(260)
    draw.left(120)
    draw.forward(260)
    draw.left(120)
    draw.forward(260)
    draw.left(120)

    draw.forward(150)
    draw.left(120)
    draw.forward(180)
    draw.left(120)
    draw.forward(180)
    draw.left(120)

    draw.forward(70)
    draw.left(120)
    draw.forward(100)
    draw.left(120)
    draw.forward(100)
    draw.left(120)
  
    draw.end_fill()
    
def second_skyline():
    draw.fillcolor("chocolate")
    draw.pencolor("chocolate")
    draw.begin_fill()
    draw.forward(300)
    draw.right(90)
    draw.forward(250)
    draw.right(90)
    draw.forward(500)
    draw.right(90)
    draw.forward(250)
    draw.right(90)
    draw.forward(250)

    draw.end_fill()

def third_skyline():
    draw.fillcolor("beige")
    draw.pencolor("navy")
    draw.begin_fill()
    draw.forward(250)
    draw.left(90)
    draw.forward(250)
    draw.left(90)
    draw.forward(430)
    draw.begin_fill()
    draw.circle(50)
    draw.end_fill()


    




def main():
    turtle.bgcolor("navy")
    first_skyline()
    second_skyline()
    third_skyline() 
  
    turtle.done()
    

    """draw_skyline

    
    turtle_state()

    draw_triangle(draw,x,y,height,width,size, color)

    turtle_state()

 
    draw_circle(draw,x,y,width,size,color)
    turtle_state()

    draw_rectangle(draw,x,y,width,height,size,color)
    turtle_state()
    turtle.done()
    """
main()
