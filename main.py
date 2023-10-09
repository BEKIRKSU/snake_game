from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# All we're doing here is creating a screen. importing the snake and it's movement and
# adding a gams_is_on + while loop to it.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Always use documentation to see which methods to use.


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg_num in range(start= 2, stop= 0, step= -1):
    # for seg_num in range(start= len(segments), stop= 0, step= -1):

    snake.move()
#     After we have what we have so far, we detect the collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 270 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

#     For collision of head and any segment of tail should = game over.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

        #     The code above should work just like the code below.
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()



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