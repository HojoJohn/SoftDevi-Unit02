import turtle
angle = 45
def test_drive():

    turtle.forward(100)

    turtle.left(87)

    turtle.setheading(127)

    turtle.up()

    turtle.down()

    turtle.goto(50, 50)

    turtle.circle(25)

    input("Press enter to conitnue: ")

def turtle_state():

    turtle.isdown()

    turtle.heading()

    turtle.xcor()

    turtle.ycor()

def square(conti, angle):

    turtle.pensize(4)

    turtle.color("red")

    turtle.fillcolor("blue")

    turtle.begin_fill()

    turtle.forward(conti)

    turtle.left(conti)

    turtle.forward(conti)

    turtle.left(conti)

    turtle.forward(conti)

    turtle.left(conti)

    turtle.forward(conti)

    turtle.left(conti)

    turtle.end_fill()

    input("Press enter to conitnue: ")

def main():

    turtle_state()

    #test_drive()

    turtle.bgcolor("pink")

    square(100, angle)
    square(45, angle)


    turtle_state()

main()