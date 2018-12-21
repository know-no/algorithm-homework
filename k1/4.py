'''
Description

Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2. Append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.

Input:A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = {2, 1, 8, 3}Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

Since 2 is present first in A2[], all occurrences of 2s should appear first in A[], then all occurrences 1s as 1 comes after 2 in A[]. Next all occurrences of 8 and then all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]

Constraints:1 ≤ T ≤ 501 ≤ M ≤ 501 ≤ N ≤ 10 & N ≤ M1 ≤ A1[i], A2[i] ≤ 1000

Input

The first line of input contains an integer T denoting the number of test cases. The first line of each test case is M and N. M is the number of elements in A1 and N is the number of elements in A2.The second line of each test case contains M elements. The third line of each test case contains N elements.

Output

Print the sorted array according order defined by another array.

Sample Input 1

1
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3

Sample Output 1

2 2 1 1 8 8 3 5 6 7 9
'''

import sys

def fuck():
    tmp = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    m , n = tmp[0],tmp[-1]
    a = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    b = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    b2 = set(b)
    a2 = dict()
    tmp = []
    for i in a :
        if i in b2:
            a2.setdefault(i,0)
            a2[i] += 1
        else:
            tmp.append(i)
    answer = []
    for i in b:
        if  i in a2.keys():
            lis = a2[i]
            lis_i = [i for x in range(lis)]
            answer = answer + lis_i
    answer = answer + sorted(tmp)
    for i in answer:
        print(i,end=" ")


    
if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for s in range(t):
        fuck()