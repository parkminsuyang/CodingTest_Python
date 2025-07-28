import sys
import bisect
from bisect import bisect_left

input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))

res=[]

for i in range(n):
    idx=bisect_left(res,num[i])
    if idx==len(res):
        res.append(num[i])
    else:
        res[idx]=num[i]

print(len(res))