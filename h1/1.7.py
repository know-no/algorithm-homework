'''

Input
输入时一个数组，数值通过空格隔开。
Output
输出筛选之后的数组，用空格隔开。如果有多种结果，则一行一种结果。
Sample Input 1 
1 2 4 7 11 10 9 15 3 5 8 6
Sample Output 1
1 2 4 7 11 10 9 8 6
'''

import sys

arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]

#双端LIS问题
#先再左端LIS

#定义数组 lis_l[len(arr)]  lis_r[len()]
lis_l = [1 for i in range(len(arr))]
lis_r = [1 for i in range(len(arr))]

for i in range(1,len(arr)):
    for j in range(i-1,-1,-1):
        if arr[i] > arr[j] and lis_l[i] < lis_l[j] + 1:
            lis_l[i] = lis_l[j] + 1
            

for i in range(len(arr) - 2, -1 , -1):
    for j in range(i+1,len(arr), + 1):
        if arr[i] > arr[j] and lis_r[i] < lis_r[j] + 1:
            lis_r[i] = lis_r[j] + 1
            
# print(lis_l)
# print(lis_r)
max = 0
v = 0
for i in range(len(arr)):
    if max < lis_l[i] + lis_r[i]:
        max = lis_l[i] + lis_r[i]
        v = i

# print(max,v)
def get_l(arr,lis,index):
    if lis[index] == index + 1:
        return arr[0:index + 1]
    elif arr[index] > arr[index - 1]:
        tmp = get_l(arr,lis,index - 1)
        tmp.append(arr[index])
        return tmp
    elif arr[index] <= arr[index - 1]:
        return get_l(arr, lis, index - 1)
print(get_l(arr,lis_l,v))

def get_r(arr,lis,index):
    if lis[index] == len(arr) - index:
        return arr[index:len(arr)]
    elif arr[index] > arr[index + 1]:
        tmp = get_r(arr,lis,index + 1)
        tmp = [arr[index]] + tmp
        print(tmp)
        return tmp
    elif arr[index] <= arr[index + 1]:
        return get_r(arr, lis, index + 1)

print(get_r(arr, lis_r, v))
        
