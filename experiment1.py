import turtle
t = turtle.Turtle()


def main():

    t.speed(20)

    t.pendown()
    for i in range(160):
        t.left(10)
        tr(10+i)


def tr(a):
    for i in range(6):
        t.forward(a)
        t.left(60)

main()

t.end_fill()
t.getscreen().mainloop()
