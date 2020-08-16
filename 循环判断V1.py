a = [1,1,2,33,4,5,6,7,8,1,22]
b = []
num = int(input("请输入一个数字"))
i = 0
for i in range(len(a)):
    if a[i] < num:
        b.append(a[i])
    i += 1
print(b)
