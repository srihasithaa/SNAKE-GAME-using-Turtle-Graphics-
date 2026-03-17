from turtle import Turtle

CORS=[(0,0), (-20,0), (-40,0)]
DISTANCE=20
# 20 only because turtle size is 20x20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.body=[]
        self.create()
        self.head=self.body[0]

    def create(self):
        for loc in CORS:
            self.grow(loc)

    def move(self):
        # move body
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)

        # move head
        self.head.forward(DISTANCE)

    def grow(self,p):
        rio = Turtle("circle")
        rio.color("midnight blue")
        rio.penup()
        rio.goto(p)
        self.body.append(rio)

    def extend(self):
        self.grow(self.body[-1].position())

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.seth(DOWN)

    def lft(self):
        if self.head.heading()!= RIGHT:
            self.head.seth(LEFT)

    def rgt(self):
        if self.head.heading()!= LEFT:
            self.head.seth(RIGHT)
