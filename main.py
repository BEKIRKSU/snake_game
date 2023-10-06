from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    snake_new_segment = Turtle("square")
    snake_new_segment.color('white')
    snake_new_segment.penup()
    snake_new_segment.goto(position)
    segments.append(snake_new_segment)
# Always use documentation to see which methods to use.


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg_num in range(start= 2, stop= 0, step= -1):
    # for seg_num in range(start= len(segments), stop= 0, step= -1):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
   



# Instead of the code below, since it's repeated we could use a for look like above ^
# snake_1 = Turtle("square")
# snake_1.color("white")
#
# snake_2 = Turtle("square")
# snake_2.color("white")
# snake_2.goto(-20, 0)
#
# snake_3 = Turtle("square")
# snake_3.color("white")
# snake_3.goto(-40, 0)



screen.exitonclick()