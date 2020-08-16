import random

a = input("请出拳（石头/剪刀/布）：")
b = ["剪刀", "石头", "布"]
#定义赢的列表
win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
#计算机随机选择出圈
mac = random.choice(b)
print("你出拳：",a)
print("计算机出拳：",b)
if a in b:
    if a == mac:
        print("平局")
    elif [a,mac] in win_list:
        print("恭喜！你赢了！")
    else:
        print("很遗憾，你输了！")
else:
    print("输入错误")