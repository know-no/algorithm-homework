'''
Description

Babul’s favourite number is 17. He likes the numbers which are divisible by 17. This time what he does is that he takes a number N and tries to find the largest number which is divisible by 17, by rearranging the digits. As the number increases he gets puzzled with his own task. So you as a programmer have to help him to accomplish his task.Note: If the number is not divisible by rearranging the digits, then print “Not Possible”. N may have leading zeros.


Input

The first line of input contains an integer T denoting the no of test cases. Each of the next T lines contains the number N.


Output

For each test case in a new line print the desired output.


Sample Input 1 

4
17
43
15
16
Sample Output 1

17
34
51
Not Possible



'''

import sys
'''
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

'''
from itertools import combinations, permutations


def fun(n):
    tmp = n
    nums = []
    while tmp > 0 :
        num = tmp % 10
        nums.append(num)
        tmp = tmp // 10
    res = []

    ans = permutations(nums)
    while True:
        try:
            an = next(ans)
            t = 0
            for i in an:
                t = t * 10 + i
            res.append(t)
        except Exception :
            break

#    print(res)
    maximum = -1
    for i in res:
        if i > maximum and i % 17 == 0:
            maximum = i

    if maximum == -1:
        maximum = "Not Possible"
    
    return maximum

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip().lstrip("0"))
        res = fun(n)
        print(res)


