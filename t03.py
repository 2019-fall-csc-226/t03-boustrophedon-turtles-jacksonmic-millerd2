import turtle   #allows us to use turtle library

wn = turtle.Screen()

wn.bgcolor("red")

at = turtle.Turtle() # creates the turtle and sets its attributes
at.pensize(6)

size = 25



def build():
    """a function that will help us build a picture"""
    at.penup()
    at.setpos(-250, 250)
    at.forward(10)
    at.pendown()
    for i in range(4):
        size = 15
        size = size + 2
        at.forward(500)
        at.right(90)

def direction():
    """changes the position of the turtle"""
    at.penup()
    at.forward(10)
    at.right(90)
    at.forward(495)
    at.left(90)
    at.pendown()
    for i in range(10):

        at.forward(490)
        at.left(90)
        at.forward(2)
        at.left(90)
        at.forward(490)
        at.right(90)
        at.forward(2)
        at.right(90)
        at.forward(490)
build()
direction()
wn.exitonclick()
