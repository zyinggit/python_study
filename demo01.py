"""
print("你好，python!")
print(2222,444.56,"zhangying",(),[],{}) #打印

#()元组   []数组  {}字典

print("重头学习python"+",加油") #字符串拼接，同类型进行拼接
print("你好！"*10)#字符串只鞥进行加法和乘法运算

print(2<3)#输出True
"""

"""
a=input("请输入：")
b=input("请输入：")
print("input获取的内容：",a+b)
#无论输入什么，input()获取的都是字符串类型
"""

"""
#type()获取数据类型
print(type(23))
print(type(23.56))
print(type("你好"))
print(type(True))
print(type(()))
print(type([]))
print(type({}))
"""

"""
#数据类型转换
a=float(input("请输入数字："))
b=float(input("请输入数字："))
print("input获取的内容：",a+b)
#无论输入什么，input()获取的都是字符串类型
"""

#练习：通过代码获取两段内容，计算他们的长度和
a=input("请输入：")
b=input("请输入：")
print("第一次输入为：",a)
print("第二次输入为：",b)
print("两次输入的内容的长度之和为：",len(a)+len(b))
print("两次输入的内容的长度之和为：",len(a+b))