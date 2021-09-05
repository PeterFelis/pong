from turtle import Screen, Turtle
from display import Middenlijn, Speler, Comp, Ball, Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

screen.loopt = Turtle()
screen.loopt.pause = False

screen.middenlijn = Middenlijn()
screen.score = Score()

screen.speler = Speler(-270)
screen.comp = Comp(270)
screen.ball = Ball()

screen.ball.move()
screen.comp.move()



def go():
    if not screen.loopt.pause:
        screen.update()
    screen.ontimer(go, 50)
go()

def pause():
    screen.loopt.pause = not screen.loopt.pause
    screen.ball.move()


screen.listen()
screen.onkeypress(screen.speler.up, "Up")
screen.onkeyrelease(screen.speler.stop, "Up")
screen.onkeypress(screen.speler.down, "Down")
screen.onkeyrelease(screen.speler.stop, "Down")
screen.onkeyrelease(pause, "space")


screen.exitonclick()


