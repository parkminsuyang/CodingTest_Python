import sys
import heapq

input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[]for _ in range(n+1)]
res=[]

for _ in range(m):
    a,b=map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)

heap=[]
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)

while heap:
    x=heapq.heappop(heap)
    res.append(x)

    if graph[x]:
        for nxt in graph[x]:
            indegree[nxt]-=1
            if indegree[nxt]==0:
                heapq.heappush(heap,nxt)


print(*res)
