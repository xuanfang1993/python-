#五种食材，两两组合成不同的菜谱
diet = ['西红柿', '黄瓜', '花椰菜', '牛排', '虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
