import turtle


t = turtle.Turtle()


def main(a):
    t.speed(20)
    t.color('black')
    t.pensize(2)
    eyes(a)
    head(a)
    mouth(a)
    teeth(a)


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


def mouth(a):
    t.begin_fill()

    t.home()
    t.pendown()
    t.right(90)
    t.circle(-a, 200)
    t.left(150)
    t.forward(a)

    t.left(75)
    t.circle(a*3, 130)

    t.left(75)
    t.forward(a)
    t.left(149)
    t.circle(-a, 200)

    t.penup()

    t.fillcolor('green')
    t.end_fill()


def teeth(a):

    t.home()
    t.pendown()
    t.right(90)
    t.circle(-a, 200)
    t.left(150)
    t.forward(a)
    t.left(75)
    t.circle(a*3, 5)

    lateral_tooth(a)  # left tooth

    t.penup()
    t.right(80)
    t.circle(a * 3, 13)
    t.pendown()

    # --- middle teeth ---
    t.right(60)
    middle_tooth(a)

    t.penup()
    t.right(60)
    t.circle(a * 3, 25)
    t.pendown()

    t.right(64)
    middle_tooth(a)
    # --- middle teeth ---

    t.penup()
    t.right(60)
    t.circle(a*3, 13)
    t.pendown()

    lateral_tooth(a)  # right tooth


def lateral_tooth(a):
    t.begin_fill()
    t.right(50)
    t.circle(a*3, 15)
    t.circle(a/7, 100)
    t.left(15)
    t.circle(a*3, 12)
    t.fillcolor('white')
    t.end_fill()


def middle_tooth(a):
    t.begin_fill()
    t.circle(a, 30)
    t.circle(a / 6.5, 60)
    t.left(10)
    t.circle(a, 40)
    t.fillcolor('white')
    t.end_fill()


def body():
    t.pensize(4)
    t.color('red')

main(50)

t.end_fill()
t.getscreen().mainloop()
