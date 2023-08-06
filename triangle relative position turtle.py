import turtle
turtle.title('214G1A0522')
# create a turtle object
t = turtle.Turtle()
t.write('214G1A0522')
# set the initial position of the turtle
t.penup()
t.goto(-100, 0)
t.pendown()
# draw a triangle with relative positioning
for i in range(3):
  t.forward(200)
  t.left(120)
#(or)
# draw a triangle with relative positioning
#t.forward(200) # move 200 units forward
#t.left(120) # turn left 120 degrees
#t.forward(200) # move 200 units forward
#t.left(120) # turn left 120 degrees
#t.forward(200) # move 200 units forward

