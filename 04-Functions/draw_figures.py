import turtle
import figures
# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")


figures.draw_square(100, pen)
pen.penup()
pen.goto(-150, 0)
figures.draw_square(50, pen)
pen.penup()
pen.goto(500, 0)
figures.draw_triangle(100, pen)
pen.penup()
pen.goto(0, -150)
figures.draw_triangle(50, pen)
pen.penup()
pen.goto(0, 150)
figures.draw_rectangle(150, 100, pen)
pen.penup()
pen.goto(-200, -150)
figures.draw_rectangle(75, 50, pen)
pen.penup()
pen.goto(0,0)



pen.hideturtle()
window.mainloop()