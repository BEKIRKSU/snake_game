from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-50, y=270)
        # these ^ need to be addressed before the writing happens.
        self.write(f"Score: {self.score}", align="left", font=('Arial', 24, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=('Arial', 24, 'normal'))

