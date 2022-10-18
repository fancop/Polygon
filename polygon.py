import turtle as t
import random

t.speed(0)
t.colormode(255)
t.ht()

while True:
    x = random.randint(-500, 500)
    y = random.randint(-300, 100)
    sides =random.randint(3, 10)    # спрашиает, сколько граней
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    size = random.randint(40, 60)

    t.penup()
    t.goto(x, y)


    t.fillcolor(red, green, blue)
    t.pendown()
    t.begin_fill()
    for i in range(sides):
        t.fd(size)
        t.left(360 / sides)
    t.end_fill()
t.done()