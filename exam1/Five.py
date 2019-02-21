# 5.实现以下功能：（30分）
# 	s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python ' \
# 对这段文字中的单词进行数字统计，并且进行个数升序
# （能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
#利用空格进行 字符串分割
# str = s.split(' ')
# 对这段文字中的单词进行数字统计
# print(str)
# print("文字中共有单词",str.__len__())

str = ''
for i in range(s.__len__()):
    if s[i] == ' ' or s[i] == ',' or s[i] == '.':
        continue
    str += s[i]
print(str)
sett = set(str)
print("文字中共有单词",sett.__len__())


