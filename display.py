import random
from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speler = 0
        self.comput = 0
        self.goto(0, 270)
        self.color('white')
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Speler: {self.speler}  Computer: {self.comput}",
                   move=False, align="center", font=("Arial", 16, "normal"))


class Middenlijn():
    def __init__(self):
        super().__init__()
        for i in range(-310, 300, 90):
            segment = Turtle()
            segment.shape('square')
            segment.penup()
            segment.shapesize(3, 0.4)
            segment.color('white')
            segment.goto(0, i)


class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(3, 0.4)
        self.color('white')
        self.goto(xpos, 0)
        self.speed(0)
        self.moving = 'geen'
        self.stap = 15
        self.x = 0
        self.y = 0
        self.getscreen().update()


class Speler(Paddle):
    def __init__(self, xpos):
        Paddle.__init__(self, xpos)
        self.move()

    def up(self):
        self.moving = 'up'

    def down(self):
        self.moving = 'down'

    def stop(self):
        self.moving = 'geen'

    def move(self):
        self.y = self.pos()[1]
        self.x = self.pos()[0]

        if self.moving == 'up':
            self.y += self.stap
            if self.y > 300:
                self.y = 300

        if self.moving == 'down':
            self.y -= self.stap
            if self.y < -300:
                self.y = -300

        if self.distance(self.getscreen().ball.pos()) < 30:
            self.getscreen().ball.kaatsen()

        self.goto(self.x, self.y)
        self.getscreen().ontimer(self.move, 25)


class Comp(Paddle):
    def __init__(self, xpos):
        super().__init__(xpos)
        self.moving = 'up'
        self.move()

    def move(self):
        y = self.pos()[1]
        x = self.pos()[0]
        yball = self.getscreen().ball.pos()[1]

        if yball > y:
            self.stap = abs(self.stap)
        else:
            self.stap = -abs(self.stap)

        self.goto(x, y + self.stap)

        if self.distance(self.getscreen().ball.pos()) < 50:
            self.getscreen().ball.kaatsen()

        self.getscreen().ontimer(self.move, 50)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.xmove = 10
        self.ymove = 20
        self.xpos = 0
        self.ypos = 0

        self.shape('circle')
        self.penup()
        self.shapesize(2, 2)
        self.color('yellow')

        self.move()

    def kaatsen(self):
        self.xmove = 1 - self.xmove

    def move(self):
        # bal van het scherm
        if self.xpos > 300 or self.xpos < -300:
            if self.xpos > 300:
                self.getscreen().score.speler += 1
            else:
                self.getscreen().score.comput += 1

            self.xpos = 0
            self.ypos = 0
            self.ymove = random.randint(-15, 15)
            self.getscreen().score.update_score()

        # ball horizontaal verplaatsen
        self.xpos += self.xmove

        #bal tussen paddles
        #omkeren vert beweging
        if self.ypos > 280 or self.ypos < -280:
            self.ymove = -self.ymove

        #ball verticaal verplaatsen
        self.ypos += self.ymove

        self.goto(self.xpos, self.ypos)

        self.getscreen().ontimer(self.move, 50)
