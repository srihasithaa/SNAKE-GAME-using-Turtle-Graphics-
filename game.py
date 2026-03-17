import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

scr=Screen()
scr.setup(width=700, height=700)
scr.bgcolor("light blue")
scr.title("Snake Game 🐍")
scr.tracer(0)

venom=Snake()
pie=Food()
pts=Score()

scr.listen()
scr.onkey(venom.up, "Up")
scr.onkey(venom.down, "Down")
scr.onkey(venom.lft, "Left")
scr.onkey(venom.rgt, "Right")

game=True

while game:
    scr.update()
    time.sleep(0.1)

    venom.move()

    # detect collision with food
    if venom.head.distance(pie)<15:
        pie.refresh()
        venom.extend()
        pts.update()

    # detect collision with wall
    if venom.head.xcor()>340 or venom.head.xcor()<-340 or venom.head.ycor()>340 or venom.head.ycor()<-340:
        game=False
        pts.over()

    # detect collision with tail
    for part in venom.body[1:]:
        if venom.head.distance(part)<10:
            game=False
            pts.over()


scr.exitonclick()