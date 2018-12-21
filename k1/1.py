'''
Description

Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}. If frequencies of two elements are same, print them in increasing order.

Input

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.（1 ≤ T ≤ 70；30 ≤ N ≤ 130；1 ≤ A [ i ] ≤ 60 ）

Output

Print each sorted array in a seperate line. For each array its numbers should be seperated by space.

Sample Input 1

1
5
5 5 4 6 4

Sample Output 1

4 4 5 5 6
'''

import sys

def fuck():
    
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    # print(t,n,a)
    cp = dict()
    times = [0 for i in range(61)]

    for i in range(len(a)):
        times[a[i]] += 1
        cp.setdefault(times[a[i]],set())
        cp[times[a[i]]].add(a[i])
        if times[a[i]] - 1 in cp:
            cp[times[a[i]] - 1].remove(a[i])

    keys=[]
    for k in cp.keys():
        keys.append(k)


    keys = sorted(keys,reverse=True)
    # print(keys)
    for k in keys:
        tmp = list(cp[k])
        sorted(tmp)
        for i in range(len(tmp)):
            for j in range(k):
                print(tmp[i],end=" ")

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for s in range(t):
        fuck()