from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,310)
        self.change()

    def change(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score+=1
        self.clear()
        self.change()

    def over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
