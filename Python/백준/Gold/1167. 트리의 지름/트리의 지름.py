import sys
from collections import deque

v=int(input())
graph=[[] for _ in range(v+1)]

for i in range(v):
    data=list(map(int,input().split()))

    index=0
    start=data[index]
    index+=1
    while True:
        now=data[index]
        if now==-1:
            break
        graph[start].append((now,data[index+1]))
        index+=2


visited=[False]*(v+1)
r = [0] * (v + 1)

def BFS(i):
    queue=deque()
    queue.append(i)

    visited[i]=True

    while queue:
        q=queue.popleft()

        for j in graph[q]:
            if not visited[j[0]]:
                visited[j[0]]=True
                queue.append(j[0])
                r[j[0]]=r[q]+j[1]

BFS(1)
m=1
for i in range(2,v+1):
    if r[m]<r[i]:
        m=i

visited=[False]*(v+1)
r = [0] * (v + 1)

BFS(m)
print(max(r))
