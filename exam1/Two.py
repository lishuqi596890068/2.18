import random
list = []
# 包含50个随机整数的列表
for i in range(50):
    list.append(random.randrange(-10,10))#随机生成整数 范围是-10到10
print(list)
listZ = []
listF = []
for i in range(len(list)):
    if list[i] >= 0:
        # 然后将列表中所有的正数存为一个新的子列表，
        listZ.append(list[i])
    elif list[i] < 0:
        # 负数存为另一个新的子列表。
        listF.append(list[i])
print(listZ)
print(listF)

