import turtle
colors = ["red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(100)
for x in range(100):
    my_pen.pencolor(colors[x%6])
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(90)

