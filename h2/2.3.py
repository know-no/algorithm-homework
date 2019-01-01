import sys

def fun(length , nums , k):
    end = 0
    start = end + k - 1
    while end < length:
        for i in range(start , end - 1 , -1):
            print(nums[i],end=" ")
        end += k 
        start = end + k - 1 if end + k - 1 < length else length - 1

if __name__=="__main__":
    for x in sys.stdin:
        tmp = [i for i in x.strip().split(" ")]
        fun(int(tmp[0]), tmp[1:-1],int(tmp[-1]))
        print() 
