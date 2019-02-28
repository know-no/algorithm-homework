'''


Description

There are Infinite People Standing in a row, indexed from 1.A person having index 'i' has strength of (i*i).You have Strength 'P'. You need to tell what is the maximum number of People You can Kill With your Strength P.You can only Kill a person with strength 'X' if P >= 'X' and after killing him, Your Strength decreases by 'X'.

Input

First line contains an integer 'T' - the number of testcases,Each of the next 'T' lines contains an integer 'P'- Your Power.Constraints:1<=T<=100001<=P<=1000000000000000

Output

For each testcase Output The maximum Number of People You can kill.

Sample Input 1

1
14

Sample Output 1

3


'''
import sys
def max_number(p):
    ans = 0
    i = 1
    while True:
        p = p - i*i
        if p >= 0:
            ans += 1
            i += 1
        else:
            break
    return ans
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    while n>0:
        n = n - 1
        p = int(sys.stdin.readline().strip())
        num = max_number(p)
        print(num)
