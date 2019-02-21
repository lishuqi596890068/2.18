# 编写程序，生成一个包含20个随机整数的列表，
# 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
# 奇数下标的元素不变。（提示：使用切片。） (20
# 分：生成列表5分，找到偶数下标8分，降序7分)
import random
list = []
for i in range(20):
    list.append(random.randrange(50))
    # 生成一个包含20个随机整数的列表，
print(list)
oulist = []
for i in range(len(list)):
    if i%2==0:
        # 找到偶数下标8分
        oulist.append(list[i])

oulist.sort()
oulist.reverse()
print(oulist)
