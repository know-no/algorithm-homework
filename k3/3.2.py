'''
Description

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only first such pair.

NOTE: A solution will always exist, read Goldbach’s conjecture.Also, solve the problem in linear time complexity, i.e., O(n).


Input

The first line contains T, the number of test cases. The following T lines consist of a number each, for which we'll find two prime numbers.Note: The number would always be an even number.


Output

For every test case print two prime numbers space separated, such that the smaller number appears first. Answer for each test case must be in a new line.


Sample Input 1

5
74
1024
66
8
9990
Sample Output 1

3 71
3 1021
5 61
3 5
17 9973
'''


import sys

import math

def fun(n):
    for i in range(2 , n - 1):
        if judge(i) and judge(n - i):
            return str(i) +" " + str(n - i)
    return ""

def judge(n):
    if n <= 3:
        return True
    else:
        tmp =int(math.sqrt(n))
        for i in range(2, tmp + 1):
            if n % i == 0:
                return False
    return True
    
if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        res = fun(n)
        print(res)
