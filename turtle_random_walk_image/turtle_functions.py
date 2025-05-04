import random

turns = [0, 90, 180, 270]

"""Generate random movement."""
def random_walk(turtle):
    turtle.forward(25)
    turtle.setheading(random.choice(turns))

"""Generate random RGB values.."""
def random_color():
    r=random.random()
    g=random.random()
    b=random.random()
    return r, g, b
