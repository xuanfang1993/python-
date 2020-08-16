t = input("请输入您的货币，以$或者￥结尾:")
dollar = 0
renminbi = 0

if t[-1] == "$":
    renminbi = eval(t) * 6
    print("您的货币可以兑换{:%d}元人民币".format(renminbi))

if t[-1] == "￥":
    dollar = eval(t)/6
    print("您的货币可以兑换{:%d}美元".format(dollar))
