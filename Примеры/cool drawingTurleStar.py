import turtle

a = turtle.Turtle()
a.getscreen().bgcolor('Black')

a.penup()
a.goto(-200,100)
a.pendown()
a.color('Yellow')

a.speed(25)
def start(turtle, size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            start(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()

start(a, 360)
turtle.done()
