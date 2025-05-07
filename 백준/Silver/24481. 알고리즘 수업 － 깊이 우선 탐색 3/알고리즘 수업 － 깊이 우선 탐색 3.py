#무방향, 1~n, 가중치는 1,
#r~  깊이 우선 탐색 트리에 있는 모든 노드의 깊이 출력
#인접 정점 오름차순 방문
import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for j in range(len(graph)):
    graph[j].sort()


cnt=0
result=[-1]*(n+1)

def dfs(v,graph,visited):
    visited[v]=True
    for k in graph[v]:
        if not visited[k]:
            result[k] = result[v] + 1
            dfs(k,graph,visited)



result[r]=0
dfs(r,graph, visited)
for f in range(1,n+1):
    print(result[f])



