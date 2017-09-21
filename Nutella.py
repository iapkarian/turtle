import turtle
t = turtle.Turtle()


def main(a):
    t.speed(50)
    t.color('black')
    t.pensize(2)
    pot(a)
    eyes(a)
    mouth(a)
    nut_text(a)


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


def eyes(a):
    t.home()
    t.penup()
    t.right(90)
    t.forward(a * 0.1875)
    t.left(90)
    t.forward(a / 4)
    apple(a)
    t.forward(-a / 2)
    apple(a)


def apple(a):
    t.pendown()
    t.circle(a / 10)
    t.penup()


def mouth(a):
    t.home()
    t.penup()
    t.right(90)
    t.forward(a * 0.1875)
    t.left(90)
    t.pendown()

    t.begin_fill()
    # t.fillcolor('red')
    t.forward(a / 10)
    t.right(90)
    t.forward(a / 16)
    t.circle(-a / 10, 180)
    t.forward(a / 16)
    t.right(90)
    t.forward(a / 10)
    t.end_fill()

    # t.penup()


def nut_text(a):
    t.home()
    t.penup()
    t.forward(-a / 2)
    t.left(90)
    t.pendown()
    # t.forward(a / 10)
    # t.write('n')
    t.color('red')
    t.write('Nutella', font=('Arial', 72))


main(300)

t.getscreen().mainloop()
