import turtle


t = turtle.Turtle()


def main(a):
    t.speed(20)
    t.color('black')
    eyes(a)
    head(a)


def eyes(a):
    t.right(90)
    t.circle(a)
    t.penup()
    t.goto(-a*2, 0)
    t.pendown()
    t.circle(a)
    t.penup()

    t.home()
    t.goto(a/3, a/10)
    t.right(90)
    apple_of_the_eye(a)
    t.goto(-a/1.5, a/10)
    apple_of_the_eye(a)


def apple_of_the_eye(a):
    t.pendown()
    apple_height = a/5
    apple_width = a

    t.begin_fill()
    for i in range(2):
        t.forward(apple_width/2)
        t.circle(apple_height/4, 90)
        t.forward(apple_height/2)
        t.circle(apple_height/4, 90)
    t.forward(apple_width/2)
    t.fillcolor('black')
    t.end_fill()
    t.penup()


def head(a):
    t.begin_fill()
    t.color('green')

    t.home()
    t.left(90)
    t.pendown()
    t.circle(a, 90)
    t.right(135)
    t.circle(-a*2, 30)
    t.circle(a/5, 90)
    t.circle(-a/3, 210)
    t.circle(-a/5, 80)
    t.circle(a/4, 85)
    t.left(85)
    t.circle(-a*4, 16)
    t.left(198)
    t.circle(a, 100)
    t.home()
    t.penup()

    t.fillcolor('green')
    t.end_fill()


main(50)

t.end_fill()
t.getscreen().mainloop()
