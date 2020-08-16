# drawDigits.py
# 输入任意一个数字，显示倒计时。嵩天老师视频课程的举一反三的小例子。
import turtle


def drawGap():
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def number(x):
    for i in range(x, -1, -1):
        drawDigit(i)
        # 打印完一个数字就会清屏
        turtle.clear()
        turtle.goto(0, 0)


def drawDigit(i):
    drawLine(True) if i in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if i in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if i in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if i in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if i in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if i in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if i in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def main():
    turtle.setup(800, 600)
    turtle.pencolor('blue')
    turtle.speed(5)
    turtle.penup()
    turtle.fd(0)
    turtle.pensize(5)

# 从5开始倒计时
number(5)
turtle.hideturtle()
turtle.done()

main()