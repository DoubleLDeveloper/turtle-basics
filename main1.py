# First Code using trinket.io/turtle
# by Laura Lang
# 12-9-2023

import turtle

print("Hello World")

space = 120
turtle.pensize(10)

def draw_triangle(color, length, angle):
  turtle.color(color)
  turtle.forward(length)
  turtle.right(angle) 
  turtle.forward(length)
  turtle.right(angle) 
  turtle.forward(length)
  turtle.right(angle) 

draw_triangle("black", 120, 120)
turtle.right(space)
draw_triangle("black", 120, 120)
turtle.right(space)
draw_triangle("black", 120, 120)

draw_triangle("red", 105, 120)
turtle.right(space)
draw_triangle("red", 105, 120)
turtle.right(space)
draw_triangle("red", 105, 120)

draw_triangle("orange", 90, 120)
turtle.right(space)
draw_triangle("orange", 90, 120)
turtle.right(space)
draw_triangle("orange", 90, 120)

draw_triangle("yellow", 75 , 120)
turtle.right(space)
draw_triangle("yellow", 75 , 120)
turtle.right(space)
draw_triangle("yellow", 75 , 120)

draw_triangle("green", 60 , 120)
turtle.right(space)
draw_triangle("green", 60 , 120)
turtle.right(space)
draw_triangle("green", 60 , 120)

draw_triangle("blue", 45 , 120)
turtle.right(space)
draw_triangle("blue", 45 , 120)
turtle.right(space)
draw_triangle("blue", 45 , 120)

draw_triangle("violet", 30 , 120)
turtle.right(space)
draw_triangle("violet", 30 , 120)
turtle.right(space)
draw_triangle("violet", 30 , 120)

#TODO Make this code more DRY with lists and loops
