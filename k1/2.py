'''

Description

Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.

Input

The first line of input contains an integer T denoting the no of test cases . Then T test cases follow . Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .(1<=T<=100;1<=N<=100;1<=A[] <=1000)

Output

For each test case in a new line output will be an integer denoting minimum umber of swaps that are required to sort the array.

Sample Input 1

2
4
4 3 2 1
5
1 5 4 3 2

Sample Output 1

2
2

'''

import sys

def fuck():
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    
    
    time = 0
    for i in range(n):
        # print("i",i)
        min = a[i]
        index = i
        for j in range(i,n):
            # print(j)
            if a[j] < min:
                min = a[j]
                index = j
        if index != i:
            time += 1
            a[index] ,a[i] = a[i], a[index]
    print(time)

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for s in range(t):
        fuck()