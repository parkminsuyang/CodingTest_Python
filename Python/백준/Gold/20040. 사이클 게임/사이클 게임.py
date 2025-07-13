import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
parent=[i for i in range(n)]

def find(x):
    if parent[x]!=x:
       parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    parent_x=find(x)
    parent_y=find(y)

    if parent_x==parent_y:
        return False
    else:
        parent[parent_y]=parent_x

for i in range(m):
    a,b=map(int,input().split())
    if union(a,b)==False:
        print(i+1)
        exit()
print(0)
