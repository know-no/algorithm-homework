import sys



def bubble_sort(length , nums):
    
    for i in range(length):
        for j in range(length - 1 , i , - 1):
            if nums[j] < nums[j - 1]:
                nums[j] , nums[j - 1] = nums[j - 1] , nums[j]

    return nums


if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [ int(i) for i in x.strip().split(" ")]
        tmp = bubble_sort(tmp[0], tmp[1:])
        for i in tmp:
            print(i,end=" ")
        print()
