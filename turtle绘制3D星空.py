from turtle import *
from random import random,randint
screen = Screen()
width, height = 800,600
screen.setup(width,height)
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)
t = Turtle(visible = False, shape = "circle")
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width/2, randint(-height/2, height/2))
stars = []
for i in range(200):
    star.t.clone()
    s = random() /3
    star.pensize(s,s)
    star.speed(int(s*10))
    star.setx()