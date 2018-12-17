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
    print(new_arr)

def fuck_quick(arr,low,high):
    if low >= high :
        return
    j = fuck_partition(arr,low,high)
    fuck_quick(arr,low,j-1)
    fuck_quick(arr,j+1,high)

def fuck_partition(arr,low,high):
    l = low + 1
    h = high

    comparable = arr[low]
    while True:
        while arr[l] < comparable:
            if l == h:
                break
            l += 1
        while arr[h] > comparable:
            h -= 1
            if l == h:
                break
        if l >= h:
            break
        arr[l] , arr[h] = arr[h] ,arr[l]
    arr[low],arr[h] = arr[h] ,arr[low]
    return h

if __name__ == "__main__":
    arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    width = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    k = int(sys.stdin.readline().strip())
    # fuck_quick(arr,0,len(arr) - 1)
    fuck(arr,width,k)