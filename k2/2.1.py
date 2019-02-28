'''

Description

You are given N number of books. Every ith book has Pi number of pages. You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations, and print this minimum value. Each book will be allocated to exactly one student. Each student has to be allocated atleast one book.

Input

The first line contains 'T' denoting the number of testcases. Then follows description of T testcases:Each case begins with a single positive integer N denoting the number of books.The second line contains N space separated positive integers denoting the pages of each book.And the third line contains another integer M, denoting the number of studentsConstraints:1<= T <=70，1<= N <=50，1<= A [ i ] <=250，1<= M <=50，Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding)

Output

For each test case, output a single line containing minimum number of pages each student has to read for corresponding test case.

Sample Input 1

1
4
12 34 67 90
2

Sample Output 1

113



'''

import sys

def fun(length , nums , m):
    ma = -1
    su = 0
    n = length
    for i in nums:
        ma = max(ma,i)
        su += i
    
    l = ma
    r = su
    mid = 0

    while l < r:
        su = 0
        cnt = 0
        mid = (l + r) //2
        for i in range(n ):
            su += nums[i]
            if(su > mid):
                cnt += 1
                su = 0
                i -= 1
                continue
        cnt += 1
        if cnt > m:
            l = mid + 1
        else:
            r = mid - 1
    print(r)



if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        tmp = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        m = int(sys.stdin.readline().strip())
        fun(n, tmp, m)

