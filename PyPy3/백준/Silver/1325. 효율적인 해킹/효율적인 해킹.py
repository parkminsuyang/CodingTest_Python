import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited = [0] * (n + 1)
res=[]
visited_mark=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

def bfs(start):

    queue=deque([start])
    global visited_mark
    visited_mark+=1
    visited[start]=visited_mark
    cnt=1

    while queue:
        cur=queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt]!=visited_mark:
                cnt+=1
                visited[nxt]=visited_mark
                queue.append(nxt)
    return cnt

for i in range(n):
    res.append(bfs(i+1))


max_res=max(res)

for i in range(n):
    if res[i]==max_res:
        print(i+1,end=' ')
