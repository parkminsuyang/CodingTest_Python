import sys
input=sys.stdin.readline
n,m=map(int,input().split())
parent=[i for i in range(n+1)]
def find (x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
        return parent[x]
    return parent[x]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        parent[parent_b]=parent_a
        return True
    return False



for _ in range(m):
    d,a,b=map(int,input().strip().split())
    if d==0:
        #합치기
        union(a,b)
    else:
        #같 다 출력
        if find(a)==find(b):
            print("yes")
        else:
            print("no")
