from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

# Always use documentation to see which methods to use.


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg_num in range(start= 2, stop= 0, step= -1):
    # for seg_num in range(start= len(segments), stop= 0, step= -1):

    snake.move()




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