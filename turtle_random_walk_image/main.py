from turtle import Turtle, Screen
from turtle_functions import random_walk, random_color

tim = Turtle()
tim.color('white')
tim.speed(10)
tim.pensize(8)

"""Generate random walk."""
for _ in range(250):
    random_walk(tim)
    tim.pencolor(random_color())

screen = Screen()
screen.exitonclick()
