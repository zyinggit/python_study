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

"""
#练习：通过代码获取两段内容，计算他们的长度和
a=input("请输入：")
b=input("请输入：")
print("第一次输入为：",a)
print("第二次输入为：",b)
print("两次输入的内容的长度之和为：",len(a)+len(b))
print("两次输入的内容的长度之和为：",len(a+b))
"""

"""
#元组，下标从0开始
a=(23,24,25,"你好吗？","fine","哈哈","哈哈",True,"哈哈",False)
print(a)
print(a[3])
print(a.index("fine"))
print(a.index("哈哈"))
print(a.count("哈哈"))
"""

"""
#二维元组
a=(23,24,25,"你好吗？","fine","哈哈","哈哈",True,"哈哈",False)
b=(a,"哈哈","xixi")
#print(b)
#print(b[1])
#print(b[0])
#print(b[0][3])
print(a[0:5])  #切片   下标遵循"左闭右开"原则
print(a[-1])
print(a[:4])
"""

"""
#数组
a=[23,24,25,"你好吗？","fine","哈哈","哈哈",True,"哈哈",False]
print(a)
a.append("世界")
print(a)
a.insert(4,"我很好")
print(a)
#c=a.pop(5)
#print(c)
a1=["学习","健身"]
a.extend(a1)
print(a)
a.clear()
print(a)
"""

"""
#字典  值没有顺序，结构必须是键值对
a={
    "name":"张三",
    0:"哈哈",
    "age":24
}
#取值
print(a["name"])
#新增
a["high"]="183cm"
print(a)
#修改
a["name"]="李四"
print(a)

b=a.get("name")#取值
print(b)
c=a.pop("name")#
print(c)
print(a)
a.update(name="小花")#新增或者修改，若key存在，则修改，若不存在，则新增
print(a)

#del 删除
del a["name"] #字典通过key删除
print(a)
a2=[11,12,13,114]
del a2[2]   #数组通过下标删除
print(a2)
"""
#练习：获取用户输入的个人信息，并且保存在字典中。个人信息包括：name,age,sex
name=input("请输入姓名：")
age=input("请输入年龄：")
sex=input("请输入性别：")
info={
    "name":name,
    "age":age,
    "sex":sex
}
print("获取的用户信息为：",info)