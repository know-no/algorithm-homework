import sys
def fun(length , nums , k):
    end = 0
    start = end + k - 1
    ans = ""
    while end < length:
        for i in range(start , end - 1 , -1):
            ans = ans + str(nums[i]) + " "
        end += k 
        start = end + k -1 
        if start  >= length:
            break
    for j in range(end,length,1):
        ans += str(nums[j]) + " "

    ans = ans.strip()
    print(ans)

if __name__=="__main__":
    for x in sys.stdin:
        tmp = [i for i in x.strip().split(" ")]
        fun(int(tmp[0]), tmp[1:-1],int(tmp[-1]))
