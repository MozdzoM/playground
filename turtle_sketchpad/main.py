from turtle import Turtle, Screen

color_list=["black", "red", "green", "blue"]
color_num = 0
current_color = color_list[color_num]

def move_forward():
    tim.forward(10)

def move_backward():
    tim.pencolor("white")
    tim.back(10)
    tim.pencolor(current_color)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def change_color():
    global color_num, current_color
    color_num += 1
    if color_num >= len(color_list):
        color_num = 0
    current_color = color_list[color_num]
    tim.color(current_color)

def clear_screen():
    tim.teleport(0, 0)
    tim.clear()

tim = Turtle()
tim.shape("turtle")
tim.pensize(4)

screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key=']', fun=change_color)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
