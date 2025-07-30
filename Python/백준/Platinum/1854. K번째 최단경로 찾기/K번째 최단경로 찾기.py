import heapq
import sys

input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

distance=[[] for _ in range(n+1)]

def dijkstra():

    heap=[]
    heapq.heappush(heap,(0,1))
    heapq.heappush(distance[1],0)

    while heap:
        dist,cur=heapq.heappop(heap)

        for nxt,cost in graph[cur]:
            new_cost=dist+cost
            if len(distance[nxt])<k:
                heapq.heappush(distance[nxt],-new_cost)
                heapq.heappush(heap,(new_cost,nxt))
            else:
                if -distance[nxt][0]>new_cost:
                    heapq.heappop(distance[nxt])
                    heapq.heappush(distance[nxt], -new_cost)
                    heapq.heappush(heap, (new_cost, nxt))

dijkstra()

for i in range(1,n+1):
    if len(distance[i])==k:
        print(-distance[i][0])
    else:
        print(-1)
