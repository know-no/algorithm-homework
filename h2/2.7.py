'''
非递归的快排的实现
'''

import sys

def quick_sort(length, nums):
    
    for i in [pow(2,x) for x in range(length)]:

        for j in range(0,length,i):
            sort_partition(nums, j, j + i- 1)

    print(nums)

        



def sort_partition(arr,low,high):
    l = low
    h = high
    comparable = arr[low]
    while l < h:
       #将列表中 小于等于枢轴值的，移动到左边
       #下面的两个while中大小判断加 = 都是可以通过的 
        while arr[h] > comparable and l < h:
            h -= 1
        # 跳出此循环，则arr[h] <= compareble,
        arr[l] = arr[h]
      #将列表中 大于枢轴值的，移动到右边
        while arr[l] <= comparable and l < h:
            l += 1
         # 跳出此循环，则arr[l] > compareble,
        arr[h] = arr[l]
    # 跳出此循环，则 l >= h, 其实是l == h ，
    # 下面的是arr[l]  return l 也可以 
    if(l > h):
        print("l > h")
    arr[h] = comparable
    return h



if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [int(i) for i in x.strip().split(" ")]
        tmp = quick_sort(tmp[0], tmp[1:])
        for i in tmp:
            print(i,end=" ")
