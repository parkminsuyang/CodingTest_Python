import sys
from collections import deque

input=sys.stdin.readline
n,s,e,m=map(int,input().split())
edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

money=list(map(int,input().split()))

new_edges=[]
for a,b,c in edges:
    new_c=-c+money[b]
    new_edges.append((a,b,new_c))

get=[-int(1e9)]*(n+1)
get[s]=money[s]

for i in range(n-1):
    for cur,nxt,cost in new_edges:
        if get[cur]!=-int(1e9):
            if get[nxt]<get[cur]+cost:
                get[nxt]=get[cur]+cost

cycle_nodes=set()

for cur,nxt,cost in new_edges:
    if get[cur]!=-int(1e9):
        if get[nxt] < get[cur] + cost:
            cycle_nodes.add(nxt)

graph=[[] for _ in range(n+1)]
for a,b,_ in new_edges:
    graph[a].append(b)


def bfs(start):
    visited=[False]*(n+1)

    queue=deque(start)
    for node in start:
        visited[node]=True
    while queue:
        cur=queue.popleft()
        if cur==e:
            return True
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt]=True
                queue.append(nxt)
    return False


if bfs(cycle_nodes):
    print('Gee')
else:
    if get[e]==-int(1e9):
        print('gg')
    else:
        print(get[e])
