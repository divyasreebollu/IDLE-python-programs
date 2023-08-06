import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(2)

# Set the starting position of the turtle
t.setposition(0, 0)

# Draw a square using set position method
t.setposition(100, 0)
t.setposition(100, 100)
t.setposition(0, 100)
t.setposition(0, 0)

# Exit the turtle window when clicked
turtle.exitonclick()
