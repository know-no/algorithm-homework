import sys
def count_sort(length, nums):
    dic = dict()
    s = set()
    dic2 = dict()
    for i in nums:
        dic2.setdefault(i,1)
        dic.setdefault(i,0)
#	print(i)
        if i in s:
            dic2[i] += 1
        for j in s:
            if i > j and i not in s:
                dic[i] = dic[i] + dic2[j] 
#		print(dic)
            elif i < j:
                dic[j] += 1
        s.add(i)
    tmp = sorted(dic.items(),key = lambda item:item[1])
    ans = ""
    for i in tmp:
        for j in range(dic2[i[0]]):
            ans = ans + str(i[0]) + " "
    ans = ans.strip()
    print(ans)




if __name__ == "__main__":
    for x in sys.stdin:
        tmp = [ int(i) for i in x.strip().split(" ")]
        count_sort(tmp[0], tmp[1:])
