import math
dayfactor = 0.005
dayup = math.pow((1+dayfactor),365)
daydown = math.pow((1-dayfactor),365)
print("天天向上{:.2f}".format(dayup))
print('天天向下{:.2f}'.format(daydown))

