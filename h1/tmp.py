

import sys

arrs = []
for i in sys.stdin:
    if i == "\n":
        break
    arrs.append([int(x) for x in i.strip().split(" ")])

for i in range(len(arrs[0])):
    for j in range(1, len(arrs)):
        arrs[j][i] = arrs[j - 1][i] + arrs[j][i] if arrs[j][i] != 0 else 0
maximum = 0

for line in arrs:
    stack = []
    l = [0 for i in range(len(line))]
    r = [0 for i in range(len(line))]
    for index in range(len(line)):
        if(len(stack) == 0 or line[index] > line[stack[-1]]):
            stack.append(index)
            l[index] = index
            r[index] = index
        elif line[index] == line[stack[-1]]:
            l[index] = l[index - 1]
            r[index] = index
            stack.pop()
            stack.append(index)
        elif line[index] < line[stack[-1]]:
            while(len(stack) > 0 and line[index] < line[stack[-1]]):
                out = stack.pop()                
                r[out] = index - 1
                l[index] = out
                r[index] = index
                area = (r[out]  - l[out] + 1) * line[out]
                maximum = maximum if maximum > area else area
            if(len(stack) == 0 and line[index] != 0):
            
                stack.append(index)
            elif len(stack) != 0 and line[index] > line[stack[-1]]:
                stack.append(index)
                l[index] = stack[-1] + 1
                r[index] = index
            elif len(stack) != 0 and line[index] == line[stack[-1]]:
                l[index] = l[stack[-1]]
                r[index] = index
                stack.pop()
                stack.append(index)

    for now in stack:
    # while(len(stack) > 0):
        # now = stack.pop()        
        area = (r[stack[-1]] - l[now] + 1) * line[now]
        maximum = maximum if maximum > area else area
print(maximum)
