from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 280)
        self.level = 1
        self.points = 000
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(arg=f"❤{self.lives}", align="right", font=("Bebas Neue", 40, "normal"))
        self.goto(100, 280)
        self.write(arg=f"{self.points}", align="right", font=("Bebas Neue", 40, "normal"))

    def update_lives(self, lives):
        self.lives = lives
        self.update_scoreboard()

    def update_points(self, points):
        self.points += points
        self.update_scoreboard()

    def game_over_screen(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Bebas Neue", 40, "normal"))

    def ready_display(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="Ready?", align="center", font=("Bebas Neue", 40, "normal"))
        time.sleep(0.5)
        self.clear()
        self.write(arg="set...", align="center", font=("Bebas Neue", 40, "normal"))
        time.sleep(0.5)
        self.clear()
        self.write(arg="Go!", align="center", font=("Bebas Neue", 40, "normal"))
        time.sleep(0.2)
        self.clear()
        self.update_scoreboard()