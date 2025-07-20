import heapq
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
k=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance=[int(1e9)]*(v+1)
    distance[start]=0
    heap=[]
    heapq.heappush(heap,(0,k))

    while heap:
        dist,cur=heapq.heappop(heap)

        if distance[cur]<dist:
            continue

        for nxt,cost in graph[cur]:
            if distance[nxt]>dist+cost:
                distance[nxt]=dist+cost
                heapq.heappush(heap,(distance[nxt],nxt))
    return distance

distance=dijkstra(k)
for i in range(1,v+1):
    if distance[i]==int(1e9):
        print('INF')
    else:
        print(distance[i])

