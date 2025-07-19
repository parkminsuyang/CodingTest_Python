import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().strip().split())
graph=[[]for _ in range(n+1)]
indegree=[0]*(n+1)
res=[]

for _ in range(m):
    singer=list(map(int,input().strip().split()))
    for i in range(1,singer[0]):
        graph[singer[i]].append(singer[i+1])
        indegree[singer[i+1]]+=1


def bfs():
    queue=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        cur=queue.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            indegree[nxt]-=1
            if indegree[nxt]==0:
                queue.append(nxt)

bfs()
if len(res)!=n:
    print(0)
else:
    print('\n'.join(map(str,res)))