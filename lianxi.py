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
"""

"""
#练习：假设有10个学生成绩要录入到系统中，10个人分别是：张一。张二，，，，张shi
#并且名字和成绩需要对应上，而且大于60和小于60的要分开存放
#分析：名字与成绩要对应上，用字典；分开存放，用字典或者数组，数组

highscore={}#定义一个空字典，用来存放大于等于60的成绩
lowscore={}#空字典，用来存放小于60的成绩
stu_name=["张一","张二","张三","张四","张五","张六","张七","张八","张九","张十"]
a=0#控制数组下标的变化
while a<len(stu_name):
    score=int(input("请输入"+stu_name[a]+"的成绩："))
    if score>=60:
        highscore[stu_name[a]]=score#存到字典中
    else:
        lowscore[stu_name[a]]=score
    a=a+1#控制下标变化，每次循环加一
print("大于60的：",highscore)
print("小于60的：",lowscore)
"""

"""
#练习：for循环实现九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end=" ")
    print()
"""  
"""
#练习1：通过print打印，模拟一个红绿灯的功能，注意每次：红灯30次，绿灯35次，黄灯3次
light={"红灯":30,"绿灯":35,"黄灯":3}
for i in light: #遍历字典遍历的是它的key值
    for j in range(light[i]):
        print(i,"倒计时还有",light[i]-j,"秒")
"""

"""
#练习2：使用代码实现一个注册的功能，用户输入账号和密码，要求账号长度是5-8位，密码8-12位，并且账号必须以小写开头，存储到字典中，{username:password}
username=input("请输入账号：")
password=input("请输入密码：")
if len(username)>=5 and len(username)<=8:
    if username[0] in "abcdefghijklmnopkrstuvwxyz":
        if len(password)>=8 and len(password)<=12:
            print("注册成功！",{username,password})
        else:
            print("密码要求8-12位！")
    else:
        print("账号必须以小写开头！")
else:
    print("要求账号长度5-8位！")
"""
 
"""
#if语句——猜拳游戏
#1、用户输入一个石头（0）、剪刀（1）、布（2）
#2、电脑产生一个石头（0）、剪刀（1）、布（2） 随机产生
#3、判断胜负

import random
user_quan=int(input("请出拳石头（0）、剪刀（1）、布（2）："))
computer_quan=random.randint(0,2)
if (user_quan==0 and computer_quan==1) or (user_quan==1 and computer_quan==2) or (user_quan==2 and computer_quan==0):
    print("你赢了！")
elif(user_quan==computer_quan):
    print("平局")
else:
    print("你输了！")
"""

"""
i=1
total=0
# while i<=100:
#     total=total+i
#     i=i+1
# print("1-100的累加和为：",total)
while i<=100:
    if i%2==1:
        total=total+i
    i=i+1
print("1-100的奇数之和为：",total)
"""
"""
#计算1-100的累加和，并且去除50
i=1
sum=0
while i<=100:
    if i==50:
        i=i+1#一定要有这一句，否则会陷入死循环
        continue
    sum=sum+i
    i=i+1
print("1-100的累加和（去除50）为:%d"%sum)
"""

"""
#打印星星
# *
# **
# ***
# ****
# *****
i=1
while i<=5:
    print("*"*i)
    i=i+1
"""

"""
#有一邮箱地址如下:user_email = 'simagousheng@itcast.cn'
#希望从邮箱地址字符串中获取用户名和邮箱后缀名
#字符串的方法练习
#方式一：
user_email = 'simagousheng@itcast.cn'
position=user_email.find('@') # 查找 @ 位置
username=user_email[0:position] # 根据 postion 截取用户名和邮箱后缀
houzhui=user_email[position+1:]
print("该邮箱用户名为：",username)
print("邮箱后缀为：",houzhui)
#方式二
user_email2= 'simagousheng2@itcast.cn'
at_count=user_email2.count('@') # 判断 user_email 是否有多个 @
if at_count>1:
    print('邮箱地址不合法, 出现了多个@符号!')
else:
    result=user_email2.split('@')  # 根据 @ 将字符串截取为多个部分
print("用户名为：",result[0])
print("后缀为：",result[1])
"""

"""
#注册的处理流程
#获取用户注册注册名
name=input("请输入注册名称：")
#去除用户名两侧的空格
name=name.strip()
#判断字符串是否全部为字母
if not name.isalpha():
    print("注册失败！用户名必须全为字母！")
else:
    print(name,"注册成功！")
"""
