from turtle import *
import random


tim = Turtle()

tim.pensize(10)
angle = [0,90,180,360]

for i in range(30):
    
    random_color1 = random.random()
    random_color2 = random.random()
    random_color3 = random.random()
    tim.pencolor((random_color1,random_color2,random_color3))

    tim.forward(15)
    tim.right(random.choice(angle))

exitonclick()