from turtle import *
import random

colormode(255)
tim = Turtle()

tim.pensize(10)
angle = [90,180,360,270]
tim.speed(16)

for i in range(200):

    random_color1 = random.randint(0,255)
    random_color2 = random.randint(0,255)
    random_color3 = random.randint(0,255)
    tim.pencolor((random_color1,random_color2,random_color3))

    tim.forward(25)
    tim.setheading(random.choice(angle))

exitonclick()   