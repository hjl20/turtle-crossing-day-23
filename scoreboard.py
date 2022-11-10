from turtle import Turtle

FONT = ("Courier", 24, "normal")
CORNER = (-280, 250)
CENTER = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(CORNER)
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def update_score(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(CENTER)
        self.write("GAME OVER", align="center", font=FONT)
