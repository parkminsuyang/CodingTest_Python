import sys
from bisect import bisect_right, bisect_left

input=sys.stdin.readline
N=int(input())
num=sorted(list(map(int,input().split())))
M=int(input())
mum=list(map(int,input().split()))

for i in mum:
    print(bisect_right(num,i)-bisect_left(num,i),end=' ')