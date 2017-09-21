import turtle
t = turtle.Turtle()


def main(a):
    t.speed(50)
    t.color('black')
    t.pensize(2)
    pot(a)


def pot(a):
    t.home()
    t.penup()
    t.forward(a/2)

    t.pendown()

    t.begin_fill()
    t.fillcolor('white')
    t.right(90)
    t.forward(a*3/8)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a*3/4)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a*3/8)
    t.end_fill()

    t.penup()
    t.forward(a*3/8)

    t.pendown()

    t.begin_fill()
    t.fillcolor('brown')
    t.circle(-a/5, 70)
    t.right(20)
    t.forward(a - a/3.75)
    t.right(20)
    t.circle(-a/5, 70)
    t.right(90)
    t.forward(a)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(a*3/4)

    t.pendown()

    t.begin_fill()
    t.fillcolor('brown')
    t.circle(a/10, 50)
    t.forward(a/5)
    t.left(40)
    t.forward(a*5/8)
    t.left(40)
    t.forward(a/5)
    t.circle(a/10, 50)
    t.left(90)
    t.forward(a)
    t.end_fill()

    t.penup()
    t.left(90)
    t.circle(a / 10, 50)
    t.forward(a / 5)
    t.right(110)

    cap(a)


def cap(a):
    t.pendown()
    t.begin_fill()
    t.fillcolor('white')
    t.circle(a / 10, 50)
    t.left(10)
    t.forward(a / 6)
    t.circle(a / 10, 50)
    t.left(40)
    t.forward(a * 0.65)
    t.left(40)
    t.circle(a / 10, 50)
    t.forward(a / 6)
    t.left(10)
    t.circle(a / 10, 50)
    t.left(30)
    t.forward(a * 0.65)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(a / 20)
    for i in range(7):
        t.pendown()
        t.forward(a / 4.5)
        t.left(90)
        t.penup()
        t.forward(a / 20)
        t.pendown()
        t.left(90)
        t.forward(a / 4.5)
        t.right(90)
        t.penup()
        t.forward(a / 20)
        t.right(90)


main(200)

t.getscreen().mainloop()
