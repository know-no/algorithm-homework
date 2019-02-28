'''

非递归实现归并排序
'''

import sys

#定义一种通用的原地merge方法
def merge(nums , low , mid , high):
    i = low
    j = mid + 1
    aux = [0 for x in range(high + 1)]
    for k in range(low, high + 1):
        aux[k] = nums[k]
    for k in range(low, high + 1):
        if ( i > mid):
            nums[k] = aux[j]
            j += 1
        elif j > high:
            nums[k] = aux[i]
            i +=1
        elif aux[j] < aux[i]:
            nums[k] = aux[j]
            j += 1
        else:
            nums[k] = aux[i]
            i += 1
  #  return nums
    
# 递归实现
def merge_sort(nums, lo , hi ):
    if(hi <= lo):
        return
    mid = lo +(hi - lo) // 2
    merge_sort(nums , lo , mid)
    merge_sort(nums, mid + 1, hi)
    merge(nums, lo , mid , hi)


# 第一种方法 不借助于栈, 实现自底向上
def merge_sort_1(length, nums):
    aux = [0 for x in range(length)]

    size = 1
    while size < length:
        for lo in range(0, length - size, 2*size):
            merge(nums, lo , lo + size - 1 , min(lo + 2 * size - 1 , length - 1))
        size *= 2
    

if __name__=="__main__":
    for x in sys.stdin:
        tmp = [int(i) for i in x.strip().split(" ")]
        length = tmp[0]
        tmp = tmp[1:]
    #    merge_sort(tmp, 0 , length - 1)
        merge_sort_1(length , tmp)
        ans = ""
        for i in tmp:
            ans += str(i) + " "
        print(ans.strip())
