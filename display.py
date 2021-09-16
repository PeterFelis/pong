import random
from turtle import Turtle


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


class Middenlijn:
    def __init__(self):
        super().__init__()
        for i in range(-360, 270, 90):
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
        self.shapesize(3, 1)    # 3,04
        self.color('white')
        self.goto(xpos, 0)
        self.speed(0)
        self.moving = 'geen'
        self.stap = 15
        self.x = 0
        self.y = 0


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

        self.goto(self.x, self.y)



        self.getscreen().ontimer(self.move, 25)


class Comp(Paddle):
    def __init__(self, xpos):
        super().__init__(xpos)
        self.moving = 'up'

    def move(self):
        y = self.pos()[1]
        x = self.pos()[0]
        yball = self.getscreen().ball.pos()[1]

        if yball > y:
            self.stap = abs(self.stap)
        else:
            self.stap = -abs(self.stap)

        self.goto(x, y + self.stap)

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
        self.shapesize(1, 1)  # 2,2
        self.color('yellow')

    def kaatsen(self):
        self.xmove = 1 - self.xmove

    def balreset(self):
        self.xpos = 0
        self.ypos = 0
        self.ymove = random.randint(1, 40) - 20
        self.xmove = 1 - self.xmove
        self.getscreen().score.update_score()

    def move(self):
        # bal van het scherm

        if self.xpos > 300:
            self.getscreen().score.speler += 1
            self.balreset()
        elif self.xpos < -300:
            self.getscreen().score.comput += 1
            self.balreset()

        # bal tussen paddles
        # omkeren vert beweging
        if self.ypos > 280 or self.ypos < -280:
            self.ymove = -self.ymove

        # ball horizontaal verplaatsen
        self.xpos += self.xmove

        # ball verticaal verplaatsen
        self.ypos += self.ymove


        self.goto(self.xpos, self.ypos)


        # checken of paddle speler geraakt wordt
        balpos = self.pos()


        if balpos[0] < 0:    # speler kaatsen
            spelerpos = self.getscreen().speler.pos()
            if balpos[0] - spelerpos[0] < 25 and balpos[0] - spelerpos[0] > 10:  # xpos
                if abs(balpos[1]) < abs(spelerpos[1])+35 and abs(balpos[1]) > abs(spelerpos[1])-35:    # ypos
                    self.getscreen().ball.kaatsen()

        if balpos[0] > 0:       #computer kaatsen
            comppos = self.getscreen().comp.pos()
            if abs(abs(balpos[0]) - abs(comppos[0])) < 25:  # xpos
                if abs(balpos[1]) < abs(comppos[1]) + 35 and abs(balpos[1]) > abs(comppos[1]) - 35:  # ypos
                    self.getscreen().ball.kaatsen()


        if not self.getscreen().loopt.pause:
            self.getscreen().ontimer(self.move, 100)

