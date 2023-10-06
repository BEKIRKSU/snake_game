from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

snake_1 = Turtle("square")
snake_1.color("white")

snake_2 = Turtle("square")
snake_2.color("white")
snake_2.goto(-20, 0)

snake_3 = Turtle("square")
snake_3.color("white")
snake_3.goto(-40, 0)



screen.exitonclick()