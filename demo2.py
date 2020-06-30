"""
#判断  input输入的类型是字符串，获取的年龄要进行数据类型转换
age=int(input("请输入你的年龄："))
if age>60:
    print("你应该退休啦！")
elif age>30:
    print("家庭责任很重吧！")
elif age>20:
    print("一定要好好规划你的未来！")
else:
    print("一定要好好学习！")
"""

"""
age=input("请输入年龄：")
if age=="":
    print("输入不能为空")
    exit()
elif age in "0123456789":
    age=int(age)
    #print(age)
else:
    print("请输入正确的年龄！")
"""

"""
#a="12345"
a=23
if type(a) is int:
    print("是数字！")
elif type(a) is str:
    print("是字符串！")
else:
    print("其他")
"""

"""
#循环
a=1
while a<10:
    print("努力")
    a=a+1

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
highscore={}#定义一个空字典，用来存放大于等于60的成绩
lowscore={}#空字典，用来存放小于60的成绩
stu_name=["张一","张二","张三","张四","张五","张六","张七","张八","张九","张十"]
for name in stu_name:
    score=int(input("请输入"+name+"的成绩："))
    if score>=60:
        highscore[name]=score#存到字典中
    else:
        lowscore[name]=score
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
