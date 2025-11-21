import sys

input=sys.stdin.readline
n,m=map(int,input().split())
INF=100000009
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c

for k in range(1,n+1): #중간값
    for j in range(1,n+1): #시작값
        for i in range(1,n+1): #끝값
            graph[i][j] = min(graph[i][j], graph[i][k] +graph[k][j])

total=INF
res=0
for i in range(1,n+1):
    tmp=0
    for j in range(1,n+1):
        if graph[i][j] != INF:
            tmp += graph[i][j]


    if total > tmp:
        total = tmp
        res=i
print(res)