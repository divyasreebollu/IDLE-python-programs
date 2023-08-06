
import turtle

# create a turtle object
t = turtle.Turtle()

# set the initial position of the turtle
t.penup()
t.goto(100,100)
t.pendown()

# draw a square of side length 100
for i in range(4):
  t.forward(100)
  t.right(90)
