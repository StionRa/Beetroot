import turtle

loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)

turtle.exitonclick()

# import time
# import random
#
# print("This program draws shapes based on the number you enter in a uniform pattern.")
# num_str = input("Enter the side number of the shape you want to draw: ")
# if num_str.isdigit():
#     squares = int(num_str)
#
# angle = 180 - 180 * (squares - 2) / squares
#
# turtle.up
#
# x = 0
# y = 0
# turtle.setpos(x, y)
#
# numshapes = 8
# for x in range(numshapes):
#     turtle.color(random.random(), random.random(), random.random())
#     x += 5
#     y += 5
#     turtle.forward(x)
#     turtle.left(y)
#     for i in range(squares):
#         turtle.begin_fill()
#         turtle.down()
#         turtle.forward(40)
#         turtle.left(angle)
#         turtle.forward(40)
#         print(turtle.pos())
#         turtle.up()
#         turtle.end_fill()
#
# time.sleep(5)
# turtle.bye()

# turtle.title("My Turtle Program")
# turtle.bgcolor("blue")
#
# turtle.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
# turtle.begin_fill()
# turtle.circle(90)
# turtle.end_fill()
#
# polygon = turtle.Turtle()
#
# num_sides = 6
# side_length = 70
# angle = 360.0 / num_sides
#
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
#
# turtle.done()

# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")
#
#
# def sqrfunc(size):
#     for i in range(4):
#         skk.fd(size)
#         skk.left(90)
#         size = size + 5
#
#
# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)
#
# turtle.done()