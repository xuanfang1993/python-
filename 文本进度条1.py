import time
scale = 10
print("______执行开始_____")
for i in range(scale+1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.2)
print("_____执行结束_____")