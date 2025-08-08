import heapq
import sys
input=sys.stdin.readline

n=int(input())
edges=[]
for _ in range(n):
    a,b=map(int,input().split())
    s=min(a,b)
    e=max(a,b)
    edges.append((s,e))

d=int(input())
edges=[(s,e) for s,e in edges if e-s<=d]
edges.sort(key=lambda x:x[1])

q=[]
ans=0
for s,e in edges:
    heapq.heappush(q,s)
    start=e-d
    while q and q[0]<start:
        heapq.heappop(q)
    ans=max(ans,len(q))
print(ans)
