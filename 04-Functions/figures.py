###
# Draw a square
#
import turtle


def draw_square(length, pen):
    # Draw a square
    pen.pendown()
    for i in range(4):
        pen.forward(length)
        pen.right(90)



def draw_triangle(length, pen):
    # Draw a triangle
    pen.pendown()
    for i in range(3):
        pen.forward(length)
        pen.right(120)
    

    

def draw_rectangle(width, height, pen):
    # Draw a rectangle
    pen.pendown()
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
