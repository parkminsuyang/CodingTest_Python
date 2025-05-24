
import sys
from collections import deque

input=sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1)]
distance=[0]*(n+1)
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)


def BFS(i):
    res=[]
    queue=deque([i])
    visited[i]=True
    distance[i]=0

    while queue:
        q=queue.popleft()

        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                distance[i]=distance[q]+1
                if distance[i]==k:
                    res.append(i)

    if not res:
        print(-1)
    else:
        print('\n'.join(map(str,sorted(res))))


BFS(x)

