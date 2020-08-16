num = int(input("请输入一个数字："))
ls = []
for i in range(2,num):
    if num % i == 0:
        ls.append(i)
    else:
        i += 1
print(ls)