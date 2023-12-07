from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space",fun = move_forward) # no () because if you use a () then it will call a function here but we want that to happen only if space is clicked
screen.exitonclick()