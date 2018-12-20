'''
找到给定数组的给定区间内的倒数第K小的数值。
Input
输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。
Output
Sample Input 1
1 2 3 4 5 6 7
3 5
2
Sample Output 1
4
'''
import sys
def fuck(arr , width , k):
    new_arr = arr[width[0] - 1:width[1]]
    fuck_quick(new_arr,0,len(new_arr) - 1)
    print(new_arr[-k])

def fuck_quick(arr,low,high):
    if low >= high :
        return
    j = fuck_partition(arr,low,high)
    fuck_quick(arr,low,j-1)
    fuck_quick(arr,j+1,high)



def fuck_partition(arr,low,high):
    l = low
    h = high
    comparable = arr[low]
    while l < h:
        while arr[h] >= comparable and l < h:
            h -= 1
        arr[l] = arr[h]
        while arr[l] <= comparable and l < h:
            l += 1
        arr[h] = arr[l]
    if(l > h):
        print("l > h")
    arr[h] = comparable
    return h

if __name__ == "__main__":
    # arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    # width = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    # k = int(sys.stdin.readline().strip())
    a = [5,2,6,5,8,9,0,8,7,5]
    fuck_quick(a,0,len(a) - 1)
    # fuck(arr,width,k)
    print(a)
