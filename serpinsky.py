import turtle

def serpinsky(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        serpinsky(t, order-1, size/2)
        t.forward(size/2)
        serpinsky(t, order-1, size/2)
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        serpinsky(t, order-1, size/2)
        t.left(60)
        t.backward(size/2)
        t.right(60)

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("Трикутник Серпинського")

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-250, -250)
t.pendown()

serpinsky(t, order=3, size=500)

screen.mainloop()
