import sys

input=sys.stdin.readline


n=int(input())
parent=[i for i in range(n)]
edges=[]
def to_length(x):
    if x=='0':
        return 0
    elif 'a'<=x<='z':
        return ord(x)-96
    else:
        return ord(x)-38

every=0
for i in range(n):
    line=input()
    for j in range(n):
        cost=to_length(line[j])
        if cost>0:
            edges.append((cost,i,j))
            every+=cost

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    root_a=find(a)
    root_b=find(b)
    if root_a!=root_b:
        parent[root_b]=root_a
        return True
    return False

edges.sort()
use=0
cnt=0
for cost,a,b in edges:
    if union(a,b):
        use+=cost
        cnt+=1
    if cnt==n-1:
        break

if cnt==n-1:
    print(every-use)
else:
    print(-1)

