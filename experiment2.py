import turtle
from math import sqrt

t = turtle.Turtle()


def main():

    t.speed(50)
    t.color('red')

    for i in range(40):
        tr(150+i)
        t.left(10)


def tr(a):
    t.penup()
    t.forward(a*sqrt(3)/3)
    t.pendown()
    t.left(150)
    for i in range(3):
        t.forward(a)
        t.left(120)
    t.penup()
    t.forward(a * sqrt(3) / 3)
    t.pendown()

main()

t.end_fill()
t.getscreen().mainloop()
