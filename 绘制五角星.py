from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1: #pos 是位置position; abs()The abs () method returns the absolute value of x i.e. the positive distance between x and zero.
        break
end_fill()
