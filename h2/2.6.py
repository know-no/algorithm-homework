import sys

def count_sort(length, nums):
    dic = dict()
    for i in nums:
        dic.setdefault(i,0)
        for j in dic.keys():
            if i > j:
                dic[i] = dic[i] + 1
            elif i < j:
                dic[j] += 1

    tmp = sorted(dic.items(),key = lambda item:item[1])
    for i in tmp:
        print(i[0],end=" ")




if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [ int(i) for i in x.strip().split(" ")]
        count_sort(tmp[0], tmp[1:])
