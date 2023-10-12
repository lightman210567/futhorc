import turtle

def moveToNext():
    # move to the next space
    turtle.setheading(-90)
    turtle.up()
    turtle.sety(0)
    turtle.setheading(0)
    turtle.forward(75)
    turtle.down()

def drawA():
    turtle.setheading(90)
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

def drawB():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(105)
    turtle.forward(50)
    turtle.right(125)
    turtle.forward(60)
    turtle.left(105)
    turtle.forward(50)
    turtle.right(125)
    turtle.forward(50)
    moveToNext()

def drawC():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(75)
    # move the turtle back, to make the space smaller
    turtle.up()
    turtle.setheading(180)
    turtle.forward(25)
    moveToNext()

def drawD():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(140)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(140)
    # get the turtle clear of the rune
    turtle.up()
    turtle.setheading(0)
    turtle.forward(100)
    moveToNext()

def drawE():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.setheading(-90)
    turtle.forward(100)
    moveToNext()

drawA()
drawB()
drawC()
drawD()
drawE()
turtle.done()