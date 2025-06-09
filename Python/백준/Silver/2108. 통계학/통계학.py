import sys
from collections import Counter

input=sys.stdin.readline
n=int(input())

num=[int(input()) for i in range(n)]
num.sort()
cnt=Counter(num)

carry=0
rep=0
print(int(round(sum(num) / n)))

print(num[len(num)//2])

max_cnt=max(cnt.values())
max_list=[k for k,v in cnt.items() if v==max_cnt]
max_list.sort()
if len(max_list)>=2:
    print(max_list[1])
else:
    print(max_list[0])

print(num[-1]-num[0])