import sys

arr = [ int(x) for x in sys.stdin.readline().split(" ")]
w =int(sys.stdin.readline())
maxs = []
max = 0
for i in range(0,len(arr) - w + 1):
    max = 0
    for j in range(w):
        max = max if max > arr[i + j] else arr[i + j]
    maxs.append(max)
sum = 0
for i in maxs:
    sum += i

print(sum)
