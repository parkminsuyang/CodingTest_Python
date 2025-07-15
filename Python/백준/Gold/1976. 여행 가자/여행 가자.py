import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[]
parent=[i for i in range(n+1)]
for i in range(n):
    graph.append(list(map(int,input().strip().split())))

plan=list(map(int,input().split()))

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        parent[parent_b]=parent_a
    return True

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            union(i+1,j+1)

for p in range(len(plan)-1):
    if find(plan[p])!=find(plan[p+1]):
        print("NO")
        exit()
else:
    print("YES")