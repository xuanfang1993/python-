import math
dayup = math.pow((1+0.001), 365)
daydown = math.pow((1-0.001),365)
print("天天向上的话，一年后是{:.2f}".format(dayup))
print("天天向下的话，一年后是{:.2f}".format(daydown))
