import sys
import heapq

input=sys.stdin.readline
n,k=map(int,input().split())
jewel=[]
bag=[]

for _ in range(n):
    m,v=map(int,input().split())
    jewel.append((m,v))

for _ in range(k):
    bag.append(int(input()))

heap=[]
idx=0
res=0

jewel.sort()
bag.sort()

for b in bag:
    while idx<len(jewel) and jewel[idx][0]<=b:
        heapq.heappush(heap,-jewel[idx][1])
        idx+=1
    if heap:
        res+=-(heapq.heappop(heap))

print(res)