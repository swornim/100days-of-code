from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")
for i in range(4):
    tim.forward(100)
    tim.right(90)


screen_time = Screen()
screen_time.exitonclick()

