import turtle
import math

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rose Drawing using Python Turtle")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("red", "pink")
pen.pensize(2)

# Move turtle to starting position
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Begin filling the rose shape
pen.begin_fill()

# Rose equation: r = a * sin(k * theta)
a = 200   # Controls size of the rose
k = 7     # Number of petals (use odd number for full petals)

for theta in range(0, 361):
    rad = math.radians(theta)
    r = a * math.sin(k * rad)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    pen.goto(x, y)

pen.end_fill()
pen.hideturtle()

# Keep window open
turtle.done()
