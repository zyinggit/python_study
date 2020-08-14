"""
alist=range(0,4)
print(alist)
print(list(alist))
"""

"""
#如何去除列表中的重复元素？
alist=[4,2,1,3,4,3,2,1,1,3,2,3,2,2]
list1=set(alist)
print(list1)

list2=[]
for i in alist:
    if i not in list2:
        list2.append(i)
print(list2)
"""

"""
#冒泡排序
def bubble_sort(alist):
    n=len(alist)
    for j in range(0,n-1):
        count=0
        for i in range(0,n-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
        if count==0:
            return
if __name__=="__main__":
    alist=[54,26,93,17,31,44,55,20]
    bubble_sort(alist)
    print(alist)
"""

"""
#斐波那契数列 1、1、2、3、5、8、13、21、34...
#递归法 返回idx的值，缺点：只能返回某个值
def fib1(idx):
    if idx<=2:
        return 1
    else:
        return fib1(idx-1)+fib1(idx-2)
#迭代法，返回Idx位之前fib数列
def fib2(idx):
    lst=[]
    n,a,b=0,0,1
    while idx>n:
        lst.append(b)
        a,b=b,a+b
        n+=1
    return lst
#生成器法 
def fib3(idx):
    n,a,b=0,0,1
    while idx>n:
        yield b
        a,b=b,a+b
        n+=1

val=fib1(3)
print(val)
alist=fib2(3)
print(alist)
lst3=fib3(6)
print(list(lst3))
"""

"""
#对字符串进行反转
#不用任何系统方法，且时间复杂度最小
def reverse_str(input_str):
    input_str=list(input_str)
    n=len(input_str)
    i=0
    j=n-1
    while i<j:
        input_str[i],input_str[j]=input_str[j],input_str[i]
        i+=1
        j-=1
    return ''.join(input_str)
str1="abcdefgh"
result=reverse_str(str1)
print(result)
#使用系统方法
old_str="abcdefghilmn"
new_str=old_str[::-1]
print(new_str)
"""

"""
#返回字符串中第一个不重复的字母和位置
def first_str(str):
    d={}
    for i in range(len(str)):
        if str[i] in d:
            d[str[i]]+=1
        else:
            d[str[i]]=1
    for i in range(len(str)):
        if d[str[i]]==1:
            return '第一个不重复的字符是{},索引是{}'.format(str[i],i)
    return '没有不重复的字符'
s1='wwooppqq'
s2='wweerrftt'
res1=first_str(s1)
res2=first_str(s2)
print(res1)
print(res2)
"""

#存在一个数列 0 1 1 2 3 5 8 13 21 33 55 89 144 233 377...
#描述数列中的规律，此数据存在一处错误，请找出 
#从第三个数起，后面的数是前面两个数之和 错误处：33，应该是 34
a,b=0,1 
print(0,end=" ") 
while b<377:
     a,b=b,a+b 
     print(b,end=" ")