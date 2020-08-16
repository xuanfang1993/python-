name = input("请输姓名：")
print("{}同学，学好Python，前途无量！".format(name))
print("{}大侠，学好Python，大展拳脚".format(name[0]))
print("{}哥哥，学好Python，人见人爱".format(name[1:]))
#输入的姓名被当做一个字符串，利用切片的方法输出一部分内容。