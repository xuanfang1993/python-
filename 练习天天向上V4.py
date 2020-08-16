level = 1.0
n = 0.005

for i in range(360):
    if i % 30 in [1,2,3,4,5,6,7,8,9,10]:
        level = level * (1.0 + n)
    else:
        level = level

print("一年到头的结果是：{:.2f}".format(level))

