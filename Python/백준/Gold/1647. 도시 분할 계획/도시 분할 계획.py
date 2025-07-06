#최소 스패닝 트리
#비용으로 정렬
#최소비용/각 도시 내에서는 모두 연결 되게 분할

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))
graph.sort(key=lambda x:x[2])

parent=[i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    roota=find(a)
    rootb=find(b)
    if roota!=rootb:
        parent[rootb]=roota
        return True
    else:
        return False

cost=0
max_cost=0
for a,b,c in graph:
    if union(a,b):
        cost+=c
        max_cost=c

print(cost-max_cost)