import turtle
def apply(c):
    if c=="A":
        return "B-A-B"
    elif c=="B:"
        return"A+B+A"
    else:
        return c

def transform(original):
    result=""
    for c in original:
        result += apply(c)
    return result

def create_l_system(n, start):
    original = start
    for _ in range(n):
        result = transform(original)
        original = result
    return original

def draw_l_system(t,instructions, angle, lenght):
    for c in instructions:
        if c==["A", "B"]:
            t.forward(lenght)
        elif c=="-":
            t.right(angle)
        elif c=="+":
            t.left(angle)
   t.pu()
            t.goto(position)
            t.setheading(heading)
            t.pd()

def draw():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(100)
    instructions = create_l_system(4, "X")
    draw_l_system(t,instructions,25,2)
    t.left(90)
    t.pu()
    t.back(200)
    t.pd()
    t.speed(5)
    instructions = create_l_system(5, "X")
    draw_l_system(t,instructions,25,5)
    screen.exitonclick()

def draw():
    screen = turtle.Screen()
    t= turtle.Turtle()

    t.speed(1)
    instructions=create_l_system(8,"A")
    draw_l_system(t, instructions, 60, 2)

    screen.exitonclick()