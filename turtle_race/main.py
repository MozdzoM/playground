from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtle_id in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.color(colors[turtle_id])
    new_turtle.teleport(x=-280, y=y_positions[turtle_id])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        turtle.showturtle()
        if turtle.xcor() >= 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"The winner is {winning_color} turtle!")
            if winning_color == user_bet:
                print("GGs! You've won!")
            else:
                print("You've lost! Sorry ://")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)



screen.exitonclick()
