'''
Description

Given an array of strings A[ ], determine if the strings can be chained together to form a circle. Astring X can be chained together with another string Y if the last character of X is same as firstcharacter of Y. If every string of the array can be chained, it will form a circle.For eg for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"


Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.

The first line of each test case contains a positive integer N, denoting the size of the array.

The second line of each test case contains a N space seprated strings, denoting the elements of the array A[ ].

1 <= T <= 100

0 < N <= 30

0 < A[i] <= 10


Output

If chain can be formed, then print 1, else print 0.


Sample Input 1

2
3
abc bcd cdf
4
ab bc cd da
Sample Output 1

0
1
'''
