

import sys

def judge_hw(nums,length):
    mid = length // 2
    for i in range(mid):
        if nums[i] != nums[length - i - 1]:
            return False
    return True


if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [i for i in x.strip().split(" ")]
        print(judge_hw(tmp[1:],int(tmp[0])))
