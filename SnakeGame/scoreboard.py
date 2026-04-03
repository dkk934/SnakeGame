from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",15,"bold")
class Scorecount(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def scoreUpdate(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial",15,"bold"))

