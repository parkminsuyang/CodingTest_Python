import sys
input=sys.stdin.readline

n,m=map(int,input().split())
edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

distance=[int(1e9)]*(n+1)
distance[1]=0

for i in range(n-1):
    for cur,nxt,cost in edges:
        if distance[cur]!=int(1e9):
            if distance[nxt]>distance[cur]+cost:
                distance[nxt]=distance[cur]+cost

cycle=False
for cur,nxt,cost in edges:
    if distance[cur]!=int(1e9):
        if distance[nxt] > distance[cur] + cost:
            distance[nxt] = distance[cur] + cost
            cycle=True
            break


if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]==int(1e9):
            print('-1')
        else:
            print(distance[i])

