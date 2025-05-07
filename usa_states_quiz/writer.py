from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(10)

    def write_state(self, name, x, y):
        self.teleport(x, y)
        self.write(name, align=ALIGNMENT, font=FONT)
