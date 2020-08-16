from turtle import *
from random import *
from math import *

class Tree:
    def __init__(self):
        setup(1000,700)
        bgcolor(1,1,1)#背景色
        speed(10)
    #tracer(1,100) 设置绘图屏幕刷新频率，参数1设置在正常刷新频次的第参数1次刷新，参数2设置#每次刷新的时延
        tracer(0,0)
        pu()
        backward(100)
        #保证笔触箭头方向始终不向下，此处使其左转90度
        left(90)
        backward(300)
    def tree(self, n,l):
        pd()
        #阴影效果
        t = cos(radians(heading()+45)) / 8 + 0.25
        pencolor(t,t,t)
        pensize(n/1.2)
        forward(l)#画树枝
        if n > 0:
            b = random() * 15 + 10 #右分支偏转角度
            c = random() * 15 + 10 #左分支偏转角度
            d = l * (random() * 0.25 + 0.7) #下一个分支的长度
            #右转一定角度，画右分支
            right(b)
            self.tree(n - 1, d)
            #左转一定角度，画左分支
            left(b + c)
            self.tree(n-1, d)
            #转回来
            right(c)
        else:
            #画叶子
            right(90)
            n = cos