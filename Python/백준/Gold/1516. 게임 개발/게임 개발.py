import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
bime=[0]
before=[0]*(n+1)
res=[0]*(n+1)
for i in range(1,n+1):
    building=list(map(int,input().strip().split()))
    building.pop()
    bime.append(building.pop(0))
    before[i]+=len(building)
    for pre in building:
        graph[pre].append(i)

def bfs() :
    queue=deque()
    for build in range(1,n+1):
        if before[build]==0:
            queue.append(build)
            res[build]+=bime[build]
    while queue:
        cur=queue.pop()

        for nxt in graph[cur]:
            before[nxt]-=1
            res[nxt]=max(res[nxt],res[cur])
            if before[nxt]==0:
                res[nxt]+=bime[nxt]
                queue.append(nxt)



bfs()
for r in res[1:]:
    print(r)
