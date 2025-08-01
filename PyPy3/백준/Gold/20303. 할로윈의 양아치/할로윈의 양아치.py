import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())
candy=[0]+list(map(int,input().split()))

parent=[i for i in range(n+1)]

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    root_a=find(a)
    root_b=find(b)
    if root_a!=root_b:
        parent[root_b]=root_a

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

group=dict()
for i in range(1,n+1):
    root=find(i)
    if root not in group:
        group[root]=[0,0]
    group[root][0]+=1
    group[root][1]+=candy[i]

dp=[0]*(k)

for kid,sweet in group.values():
    for i in range(k-1,kid-1,-1):
        dp[i]=max(dp[i],dp[i-kid]+sweet)


print(max(dp))
