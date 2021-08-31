from turtle import Screen
from display import Middenlijn, Speler, Comp, Ball, Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

screen.middenlijn = Middenlijn()
screen.ball = Ball()
screen.speler = Speler(-270)
screen.comp = Comp(270)

screen.score = Score()


def go():
    screen.update()
    screen.ontimer(go, 50)
go()


screen.listen()
screen.onkeypress(screen.speler.up, "Up")
screen.onkeyrelease(screen.speler.stop, "Up")
screen.onkeypress(screen.speler.down, "Down")
screen.onkeyrelease(screen.speler.stop, "Down")


screen.exitonclick()


