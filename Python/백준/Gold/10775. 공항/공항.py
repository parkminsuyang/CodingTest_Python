import sys

input=sys.stdin.readline


g=int(input())
gate=[False]*(g+1)
p=int(input())
parent=[i for i in range(g+1)]
res=0

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    roota=find(a)
    rootb=find(b)
    if roota!=rootb:
        parent[roota]=rootb



for _ in range(p):
    x=int(input())
    if find(x)>0:
        union(find(x),(find(x)-1))
        res+=1
    else:
        break
print(res)
