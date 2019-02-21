#try:
#    print("请输入一个数字：")
#    user=input()
#    print(int(user)+1)
#except ValueError:
#    print("只能输入数字！")
#except (IOError,Valueerror):
#    print("文件夹错误")
#except Exception:
#    print("WRONG!")
#except ValueError:
#    print("111")
#print("hello world")
#IOError
#KeyError
#ValueError
#Exception(所有异常的基类)
# try:
#     print("a")
#     print("b")
#     raise(ValueError)
#     print("c")
# except:
#     print("我想在这里先停下来")
# else:#没有发生异常时执行的代码
#     print("这里没有发生异常哦")
# finally:#无论是否发生异常都一定要执行的语句！
#     print("你们要好好学习！")
# print("hallo world")

f = open('test.txt','w')
f.write("哈哈哈哈hahahahahah")
f = open('test.txt','r')
content = f.read(2)
print(content)
position = f.tell()
print(position)