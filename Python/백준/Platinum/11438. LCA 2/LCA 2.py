import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline


n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

LOG = (n).bit_length()

parent=[[0]*(n+1) for _ in range(LOG)]
depth=[-1]*(n+1)

q=deque()
q.append(1)
depth[1]=0

#bfs
while q:
    cur=q.popleft()
    for nxt in graph[cur]:
        if depth[nxt]==-1:
            depth[nxt]=depth[cur]+1
            parent[0][nxt]=cur
            q.append(nxt)

for k in range(1,LOG):
    for v in range(1,n+1):
        parent[k][v]=parent[k-1][parent[k-1][v]]

def lca(a,b):
    if depth[a]<depth[b]: #a가 더 깊어야 함
        a,b=b,a
    diff=depth[a]-depth[b]
    for k in range(LOG):
        if diff&(1<<k):
            a=parent[k][a]

    if a==b:
        return a
    for k in range(LOG-1,-1,-1):
        if parent[k][a]!=parent[k][b]:
            a=parent[k][a]
            b=parent[k][b]
    return parent[0][a]

m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))