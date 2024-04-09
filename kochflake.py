import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def kochflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Крижинка Коха")

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-150, 90)
t.pendown()

kochflake(t, order=3, size=300)

screen.mainloop()
