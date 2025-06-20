import sys
import heapq

input=sys.stdin.readline
n=int(input())
num=[]
for _ in range(n):
    a=int(input().strip())
    if a==0:
        if num:
            print(-heapq.heappop(num))
        else:
            print(0)
    else:
        heapq.heappush(num, -a)