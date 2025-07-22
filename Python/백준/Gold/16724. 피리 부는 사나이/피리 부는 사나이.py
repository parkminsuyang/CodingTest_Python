import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
parent=[ i for i in range(n*m)]
visited = [False] * (n * m)
dulr={'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
for _ in range(n):
    graph.append(input().strip())

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        parent[parent_b]=parent_a

#y,x
def get_index(i,j):
    return i*m+j

for i in range(n): #y
    for j in range(m): #x
        ind=get_index(i,j)
        ni=dulr[graph[i][j]][0]+i
        nj=dulr[graph[i][j]][1]+j
        if 0<=ni<n and 0<=nj<m:
            union(get_index(i,j),get_index(ni,nj))


res=set()
for i in range(n):
    for j in range(m):
        res.add(find(get_index(i,j)))

print(len(res))