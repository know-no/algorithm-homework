import sys

def insert_sort(length , nums):

    for i in range(1,length):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j] :
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp



    return nums

if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [ int(i) for i in x.strip().split(" ")]
       
        tmp = insert_sort(tmp[0], tmp[1:])
        for i in tmp:
            print(i,end=" ")
        print()
