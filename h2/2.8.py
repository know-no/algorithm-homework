'''

非递归实现归并排序
'''

import sys


# 第一种方法 不借助于栈
def merge_sort_1(length, nums):
    
if __name__=="__main__":
    for x in sys.stdin:
        tmp = [int(i) for i in x.strip().split(" ")]
        tmp = merge_sort_1(tmp[0] , tmp[1:])
        ans = ""
        for i in tmp:
            ans += str(i) + " "
        print(ans.strip())
