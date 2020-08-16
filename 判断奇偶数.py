num = int(input("Please type a number here"))
if num % 4 == 0:
    print("{} can be divided by 4!".format(num)
elif num % 2 == 0:
    print("{} is an even number!".format(num))
else:
    print("{} is an odd number!".format(num))