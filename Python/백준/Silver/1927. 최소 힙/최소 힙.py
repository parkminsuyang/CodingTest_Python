import sys
import heapq
input=sys.stdin.readline
n=int(input())
num=[]
for _ in range(n):
    a=int(input())
    if a!=0:
        heapq.heappush(num,a)
    else:
        if len(num)==0:
            print(0)
        else:
            print(heapq.heappop(num))


