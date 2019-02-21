# 1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
# 2.二 输入一个数求1！+2！+3！+4！+n！=？
# 3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# a = []
# for i in range(100,201):
#     b = 0
#     for x in range(2,i-1):
#         if i%x==0:
#             b += 1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))
# a = []
# for i in range(100,201):
#     b = 0
#     for x in range(2,i-1):
#         if i%x==0:
#             b += 1
#     if b == 0:
#         a.append(i)
# print(a)
# print(
#     len(a)
# )

# count = 0
# list = [1,2,3,4]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 print('%d%d%d'%(i,j,k))
#                 count += 1
# print(count)

# 2.二 输入一个数求1！+2！+3！+4！+n！=？
# num = int(input("请输入您想要到阶乘数"))
# sum = 0
# def jie(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         n *= jie(n-1)
#     return n
# while num > 0:
#     b = jie(num)
#     num -= 1
#     sum += b
# print(sum)
# 电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
# import random
# i = random.randrange(1,101)
# print(i)
# while 1:
#     num = int(input("请输入一个数字"))
#     if num > i:
#         print("太大了")
#         continue
#     elif num == i:
#         print("就是这个数")
#         break
#     elif num < i:
#         print("太小了")
#         continue



# 1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
f1 = 1
f2 = 2
temp = 0
sum = 0
for i in range(1,21):
    fn = f1/f2
    temp = f1
    f1 = f2
    f2 = temp + f2
    sum += fn
print("前二十项是",sum)
