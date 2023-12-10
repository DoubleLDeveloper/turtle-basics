# More fun turtle functions
# By Laura Lang
# 12-9-2023

import turtle

# Creates an odd-number pointed star in color of choice
def draw_star(color, num_sides, length):
  angle = 180 - 180 / num_sides
  turtle.color(color)
  if num_sides > 2 and num_sides % 2 == 1:
    for side in range(num_sides):
      turtle.forward(length)
      turtle.right(angle)
  else:
    print("Error: these stars must have an odd number of points")

# Creates any polygon with at least 3 sides at the (x,y) coordinates of choice
def draw_polygon(color, num_sides, length, x, y):
  angle = 360 / num_sides
  turtle.penup()
  turtle.goto(x,y)
  turtle.color(color)
  turtle.pendown()
  if num_sides > 2:
    for side in range(num_sides):
      turtle.forward(length)
      turtle.right(angle)
  else:
    print("Error: polygons must have at least 3 sides")

# Creates a 6x6 rainbow table repeating the same polygon
def draw_polygon_table(length, num_sides):
  colors = ["red", "orange", "yellow", "green", "blue", "violet"]
  x = -190 + length
  y = -190 + length
  for column in range(len(colors)):
    
    for color in colors:
      polygon(color, num_sides, length, x, y)
      y += 60
      
    x +=60
    y = -190 + length

# Creates 6x6 rainbow table with different shapes (better with smaller lengths such as 30)
def draw_changing_poly_table(length):
  colors = ["red", "orange", "yellow", "green", "blue", "violet"]
  x = -190 + length
  y = -190 + length
  num_sides = 3
  for column in range(len(colors)):
    
    for color in colors:
      polygon(color, num_sides, length, x, y)
      y += 60
      
    x +=60
    y = -180 + length
    num_sides += 1
    if num_sides > 5:     #can also do length/num_sides to even out size
        length -= 5

# Creates a spiral pattern 
def draw_spiral(length, angle):
  for i in range(length, 5, -10):
    turtle.forward(i)
    turtle.right(angle)

# Creates a clock pattern
def clock_pattern(num_sides, num_shapes):
  colors = ["red", "orange", "yellow", "green", "blue", "violet"]
  range_bound = num_sides + num_shapes
  for num_sides in range(num_sides, range_bound):
    move(50)
    polygon("red", num_sides, 100/num_sides)
    back(50)
    turtle.right(360/num_shapes)
