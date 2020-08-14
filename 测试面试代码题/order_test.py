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
#选择排序
def select_sort(alist):
    n=len(alist)
    for j in range(0,n-1):
        min_index=j
        for i in range(j+1,n):
            if alist[min_index]>alist[i]:
                min_index=i
        alist[min_index],alist[j]=alist[j],alist[min_index]
if __name__=="__main__":
    alist=[54,26,93,17,31,44,55,20]
    select_sort(alist)
    print(alist)
"""

"""
#插入排序
def insert_sort(alist):
    n=len(alist)
    for j in range(1,n):
        i=j
        while(i>0):
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else:
                break
if __name__ == "__main__":
    alist=[54,26,93,17,77,31,44,55,20]
    insert_sort(alist)
    print(alist)      
"""

"""
#希尔排序
def shell_sort(alist):
    n=len(alist)
    gap=n//2
    while gap>0:
        for j in range(gap,n):
            i=j
            while(i>0):
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                     break
        gap//=2

if __name__ == "__main__":
    alist=[54,26,93,17,77,31,44,55,20]
    shell_sort(alist)
    print(alist)      
"""

"""
#快速排序
def quick_sort(alist,first,last):
    if first>=last:
        return
    target_value=alist[first]
    low=first
    high=last
    while low<high:
        while low<high and alist[high]>=target_value:
            high-=1
        alist[low]=alist[high]
        while low<high and alist[low]<target_value:
            low+=1
        alist[high]=alist[low]
    alist[low]=target_value
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)
if __name__ == "__main__":
    alist=[54,26,93,17,77,31,44,55,20]
    print(alist)
    quick_sort(alist,0,len(alist)-1)
    print(alist)     
"""

#二分查找
#递归实现
def binary_search1(alist,item):
    n=len(alist)
    if n>0:
        mid=n//2
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            return binary_search1(alist[:mid],item)
        else:
            return binary_search1(alist[mid+1:],item)
    return False
#非递归
def binary_search2(alist,item):
    n=len(alist)
    first=0
    last=n-1
    while first<=last:
        mid=(last+first)//2
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            last=mid-1
        else:
            first=mid+1
    return False
if __name__ == "__main__":
    alist=[54,26,93,17,77,31,44,55,20]
    result1=binary_search1(alist,55)
    result2=binary_search1(alist,66)
    print(result1)
    print(result2)