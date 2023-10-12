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

def drawF():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.setheading(-90)
    for i in range(2):
        turtle.forward(25)
        turtle.left(135)
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(40)
        turtle.setheading(-90)
    turtle.forward(50)
    moveToNext()

def drawG():
    turtle.setheading(45)
    turtle.forward(100)
    turtle.setheading(135)
    turtle.up()
    turtle.sety(0)
    endPosition = turtle.position() # set the right corner as end position
    turtle.down()
    turtle.forward(100)
    turtle.up
    turtle.setpos(endPosition) # jump to the end position
    moveToNext()

def drawH():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.setheading(-90)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.setheading(-90)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(50)
    turtle.sety(100)
    turtle.setheading(-90)
    turtle.forward(100)
    moveToNext()

# drawA()
# drawB()
# drawC()
# drawD()
# drawE()
# drawF()
# drawG()
drawH()
turtle.done()