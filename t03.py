import turtle   #allows us to use turtle library

wn = turtle.Screen()

wn.bgcolor("red")

at = turtle.Turtle() # creates the turtle and sets its attributes
at.pensize(6)

size = 25
at.speed(15)


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
    at.color("green") # changes the turtle to green
    at.penup()
    at.forward(10)
    at.right(90)
    at.forward(495)
    at.left(90)
    at.pendown()
    for i in range(123):

        at.forward(480)
        at.left(90)
        at.forward(2)
        at.left(90)
        at.forward(480)
        at.right(90)
        at.forward(2)
        at.right(90)
       # at.forward(485)
build()
direction()
wn.exitonclick()
