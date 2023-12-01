import turtle 
import random
angle = 0
turtle.speed(16)
turtle.colormode(255)
while angle < 360:
    random_color1 = random.randint(0,255)
    random_color2 = random.randint(0,255)
    random_color3 = random.randint(0,255)
    turtle.pencolor((random_color1,random_color2,random_color3))
    turtle.circle(100)
    turtle.setheading(angle)
    angle += 10

print("je")
# turtle.fd(50)

# turtle.tilt(30)

# turtle.fd(50)

turtle.exitonclick()
