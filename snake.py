from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
# Constants are in capital letters and snake casing. They're useful because you won't
# need to dig around the entire body of the code to amend code, you can just change the const at the
# top of the page.


# All we're doing here is creating a snake and making it move.
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_new_segment = Turtle("square")
            snake_new_segment.color('white')
            snake_new_segment.penup()
            snake_new_segment.goto(position)
            self.segments.append(snake_new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        # self.segments[0].left(90)