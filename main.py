from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    snake_new_segment = Turtle("square")
    snake_new_segment.color('white')
    snake_new_segment.penup()
    snake_new_segment.goto(position)
    segments.append(snake_new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)

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