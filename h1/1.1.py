'''
给定数组arr和整数num，求arr的连续子数组中满足：其最大值减去最小值的结果大于num的个数。请实现一个时间复杂度为O(length(arr))的算法。
输入的第一行为数组，每一个数用空格隔开，第二行为num。
Sample Input 
3 6 4 3 2
2
Sample Output
6
'''
import sys
def fuck(arr,num):
    count = 0
    for i in range(len(arr)):
        queen = []
        queen.append(i)
        for j in range(i+1,len(arr)):
            # print(i, j)
            if len(queen) == 0 or arr[queen[-1]] < arr[j]:
                queen.append(j)
                if arr[j] - arr[queen[0]] > num:
                    count += len(arr) - j
                    break
            elif arr[queen[-1]] > arr[j]:
                if arr[queen[-1]] - arr[j] > num:
                    count += len(arr) - j
                    break
    print(count)

                     
if __name__ == '__main__':
    input_arr= [int(x) for x in sys.stdin.readline().strip().split(" ")]
    input_num = int(sys.stdin.readline().strip())
    fuck(input_arr,input_num)