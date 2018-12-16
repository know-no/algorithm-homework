'''
汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。

输入的第一行是步数
'''


import sys

steps = int(sys.stdin.readline())


def calculate_step(n):
    if n==1:
        return 2
    else:
        return 3*calculate_step(n-1) + 2
      
print(calculate_step(steps))