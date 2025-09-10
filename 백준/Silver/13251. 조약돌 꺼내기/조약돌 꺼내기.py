import math
import sys

input=sys.stdin.readline
m=int(input())
rock=list(map(int,input().split()))
k=int(input())
total=sum(rock)
cnt=0
for r in rock:
    if k>r:
        continue
    cnt+=math.comb(r,k)
print(cnt/math.comb(total,k))
