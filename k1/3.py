'''
Description

有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，即i<j但是A[i]>A[j]则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)

Input

输入有多行，第一行整数T表示为测试用例个数，后面是T个测试用例，每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。

Output

输出每一个用例的倒置个数，一行表示一个用例。

Sample Input 1

1
8
8 3 2 9 7 1 5 4

Sample Output 1

17

'''

import sys

def fuck():
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    d =[ 0 for x in range(n)]
    for i in range(1,n):
        if a[i] < a[i - 1]:
            for t in range(i):
                if a[t] > a[i]:
                    d[i] = d[i] + 1
        elif a[i] == a[i - 1]:
            d[i] == d[i - 1]
        else:
            j = i - 1
            while(a[i] > a[j ] and d[j] != 0):
                j -= 1 
            if a[i] < a[j]:
                d[i] = d[j] + 1
            else:
                d[i] == d[j]
    sum = 0
    for i in d:
        sum +=i
    print(sum)
    
if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for s in range(t):
        fuck()