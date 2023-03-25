import turtle

def draw_rect():
    screen = turtle.Screen()
    t= turtle.Turtle()

    t.speed(1)

    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

    screen.exitonclick()

def draw_star():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)
    for _ in range(5):
        t.forward(100)
        t.right(145)
    screen.exitonclick()

def draw_reg_polly():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(1)

    for _ in range(n):
        t.forward(100)
        t.left(360/n)

    screen.exitonclick()
