tel = input("请输入您的手机号")
list = []
if len(tel) == 11:#判断是否是十一位
    for i in range(len(tel)):
        if type(i) == int:#判断是否是数字
            list.append(tel[i])
        else:
            print("请输入正确的号码")
newlist = ''
for i in range(7):#截取前六位
    newlist += list[i]
if newlist.startswith('138') or newlist.startswith('159'):#验证号码段
        print("手机号码段验证成功")
else:
        print("手机号码不正确")
