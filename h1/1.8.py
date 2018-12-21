'''
调整数组使差最小

Description
有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序； 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。题目不一定要用动态规划的方法，可以尝试其他方法，本题答案有多种，可以得到任意一种答案的方案都可以。思考：可以尝试获得交换的次数，对比不同方案的交换次数和最终差值。
Input
输入为两行，分别为两个数组，每个值用空格隔开。
Output
输出变化之后的两个数组内元素和的差绝对值。
Sample Input 1 
100 99 98 1 2 3
1 2 3 4 5 40
Sample Output 1
48
'''

import sys

arr_1 = [int(x) for x in sys.stdin.readline().strip().split(" ")]

arr_2 = [int(x) for x in sys.stdin.readline().strip().split(" ")]

s = arr_1 + arr_2
a = []
b = []
f = True
while( len(s) != 0):
    cha = sys.maxsize
    index = 0
    for j in range(1,len(s)):
        if abs(s[0] -s[j]) < cha:
            cha = abs(s[0]-s[j])
            index = j
    if s[0] > s[index]:
        maximum , minimum = s[0],s[index]  
    else:
        maximum , minimum = s[index],s[0]
    if f:
        a.append(maximum)
        b.append(minimum)
        s = s[1:index] + s[index + 1:]
    else:
        b.append(maximum)
        a.append(minimum)
        s = s[1:index] + s[index + 1:]
    f = not f

print(a)
print(b)
            
import sys
a=[int(x) for x in sys.stdin.readline().strip().split(" ")]
b=[int(x) for x in sys.stdin.readline().strip().split(" ")]
length=len(a)
f=True
while f==True:
    sum_a=sum(a)
    sum_b=sum(b)
    A=sum_a -sum_b
    diff=sys.maxsize
    if A>=0:
        m,n=-1,-1
        for i in range(length):
            for j in range(length):
                x=a[i]-b[j]
                if 0<x<A and diff>abs(x-A/2):
                    diff=abs(x-A/2)
                    m,n=i,j
        if m==-1:
            f=False
        else:
            a[m],b[n]=b[n],a[m]
    if A<0:
        m,n=-1,-1
        for i in range(length):
            for j in range(length):
                x=a[i]-b[j]
                if A<x<0 and diff>abs(x-A/2):
                    f=True
                    diff=abs(x-A/2)
                    m,n=i,j
        if m==-1:
            f=False
        else:
            a[m],b[n]=b[n],a[m]
res=sum(a)-sum(b)
print(abs(res))