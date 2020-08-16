import time
scale = 50
print("执行开始".center(scale//2, '-'))
for i in range(scale+1):
    a = "_" * i
    b = " " * (scale -i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b,),end='')
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2, '-'))

