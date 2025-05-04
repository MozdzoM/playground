from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Arial", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.teleport(-230, 270)

        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.pencolor("white")
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
