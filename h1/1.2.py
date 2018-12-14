import sys

arrs = []
for i in sys.stdin:
    arrs.append([int(x) for x in i.split(" ")])

for i in range(len(arrs[0])):
    for j in range(1, len(arrs)):
        arrs[j][i] = arrs[j - 1][i] + arrs[j][i] if arrs[j][i] != 0 else 0

print(arrs)
maximum = 0
for arr in arrs:
    l = [0 for i in range(len(arr))]
    r = [0 for i in range(len(arr))]
    stack = []
    for j in range(len(arr)):
        # 当前stack 为空 并且 高度不是0， 将其压入，并且设置左边界为自身位置坐标-1,特殊点 arr[0]的左边界是 -1
        if len(stack) == 0 and arr[j] != 0:
            stack.append(j)
            l[j] = j
        # stack不为空，且当前高度高于stack的最高，将其压入，设置左边界 为坐标-1
        elif len(stack) != 0 and arr[j] > arr[stack[-1]]:
            stack.append(j)
            l[j] = j
        # stack 不为空，且当前高度小于stack的最高，于是，出栈，并且计算出来的高度代表的最大面积，比较
        elif len(stack) != 0 and arr[j] < arr[stack[-1]]:
            while(len(stack) !=0 and arr[j] < arr[stack[-1]]):
                r[stack[-1]] = j
                area = arr[stack[-1]] * (r[stack[-1]] - l[stack[-1]] + 1)
                maximum = maximum if maximum > area else area
                stack.pop()




print(maximum)