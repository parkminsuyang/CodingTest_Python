import sys
from collections import deque

input=sys.stdin.readline


n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent=[0]*(n+1)
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
            parent[nxt]=cur
            q.append(nxt)

def lca(a,b):
    if depth[a]<depth[b]: #a가 더 깊어야 함
        a,b=b,a
    da,db=depth[a],depth[b]
    while da>db:
        a=parent[a]
        da-=1

    while a!=b:
        a=parent[a]
        b=parent[b]
    return a


m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))