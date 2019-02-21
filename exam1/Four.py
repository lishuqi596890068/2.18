# 随机生成一个包含1000个字母的字符串，然后统计该字符串中每个字母的数量，
# 并输出结果（要求结果以字典方式存储）
# （20分：随机生成字符串5分，统计字母数量8分，以字典方式存储5分，输出结果2分）
import random
str = ''
for i in range(1000):
    str += random.choice('abcde')
    # 随机生成一个包含1000个字母的字符串，
print(str)
a = str.count('a')
b = str.count('b')
c = str.count('c')
d = str.count('d')
e = str.count('e')
dic = {'a':a,'b':b,'c':c,'d':d,'c':c}
print(dic)



