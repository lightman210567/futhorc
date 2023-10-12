import turtle

def moveToNext():
    # move to the next space
    turtle.setheading(-90)
    turtle.up()
    turtle.sety(0)
    turtle.setheading(0)
    turtle.forward(100)

def drawA():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(50)
    moveToNext()

drawA()
turtle.done()