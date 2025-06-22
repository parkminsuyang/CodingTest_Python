import sys
sys.setrecursionlimit(1000000)

input=sys.stdin.readline

n=int(input())
num=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    num[b].append(a)
    num[a].append(b)

parent=[0]*(n+1)

def dfs(c,p):
    parent[c]=p
    for j in num[c]:
        if j!=p:
            dfs(j,c)

dfs(1,0)

for i in range(2,n+1):
    print(parent[i])