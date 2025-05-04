from turtle import Turtle


class Street(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.draw_lines()
        self.draw_pavement()

    def draw_lines(self):
        self.pencolor("white")
        self.pensize(4)

        for y_value in range(-270, 270, 80):
            self.teleport(-300, y_value)
            for x_value in range(-280, 300, 60):
                self.teleport(x_value, y_value)
                self.forward(15)

    def draw_pavement(self):
        self.pencolor("gray40")
        self.pensize(30)
        self.teleport(-300, 285)
        self.forward(600)
        self.teleport(-300, -280)
        self.forward(600)
