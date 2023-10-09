from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-50, y=270)
        # these ^ need to be addressed before the writing happens.
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

# Functions are made to clean up any duplicate in code. Constants are made to
# clean the look of the code and to be able to alter the constant without going through the code body