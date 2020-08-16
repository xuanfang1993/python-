from math import sqrt
def getNum():#获取用户输入，使用列表作为承载数据和存储数据的数据类型
    nums = []
    iNumStr = input("请输入数字（直接输入回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（直接输入回车退出）：")
    return nums
def mean(numbers):#计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)
def dev(numbers, mean):#计算方差
    sdev = 0.0
    for num in numbers:
        sdev =  sdev + (num - mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):#计算中位数
