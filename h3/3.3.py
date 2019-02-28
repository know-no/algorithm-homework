'''
实现Shell排序
Description

实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），打印排序结果，注意不一定是最终排序结果！


Input

输入第一行表示测试用例个数，后面为测试用例，每一个用例有两行，第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。


Output

输出的每一行为一个用例对应的指定排序结果。


Sample Input 1

1
49 38 65 97 76 13 27 49 55 4
5 3
Sample Output 1

13 4 49 38 27 49 55 65 97 76
'''
import sys

def fuck():
    arr = list(map(int,sys.stdin.readline().strip().split(" ")))
    steps = list(map(int,sys.stdin.readline().strip().split(" ")))
    return arr,steps

def shell_sort(arr, steps):
    for step in steps:
        if step >= len(arr):
            continue
        for i in range(step, len(arr)):
            j = i
            while( j >= step and arr[j] < arr[j - step]):
                arr[j], arr[j - step] = arr[j - step] , arr[j]
                j -= step
    return arr

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        print(' '.join(map(str,shell_sort(*(fuck())))))