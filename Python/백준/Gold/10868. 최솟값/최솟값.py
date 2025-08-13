import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0]
tree=[0]*(4*n)
INF=int(1e9)

for _ in range(n):
    arr.append(int(input()))

def init(start,end,node):
    if start==end:
        tree[node]=arr[start]
        return tree[node]
    mid=(start+end)//2
    left_min=init(start,mid,node*2)
    right_mid=init(mid+1,end,node*2+1)
    tree[node]=min(left_min,right_mid)
    return tree[node]

def query(start,end,node,left,right):
    if right<start or left>end:
        return INF
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return min(query(start,mid,node*2,left,right),query(mid+1, end,node*2+1,left,right))

init(1,n,1)

for _ in range(m):
    a,b=map(int,input().split())
    print(query(1,n,1,a,b))
