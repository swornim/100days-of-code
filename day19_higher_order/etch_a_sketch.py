from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_right():
    tim.right(10)

def rotate_left():
    tim.left(10)
def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key = 'w', fun=move_forward)
screen.onkey(key = 's', fun=move_backward)
screen.onkey(key = 'd', fun=rotate_right)
screen.onkey(key = 'a', fun=rotate_left)
screen.onkey(key = 'q', fun=clear_screen)
screen.exitonclick()
