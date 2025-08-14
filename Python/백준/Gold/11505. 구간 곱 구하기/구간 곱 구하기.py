import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=[0]
tree=[0]*(4*n)
MOD=1000000007

for _ in range(n):
    arr.append(int(input()))

def init(start,end,node):
    if start==end:
        tree[node]=arr[start]%MOD
        return tree[node]
    mid=(start+end)//2
    le=init(start,mid,node*2)
    ri=init(mid+1,end,node*2+1)
    tree[node]=((le*ri)%MOD)
    return tree[node]

def update(start,end,node,idx,val):
    if idx<start or idx>end:
        return
    if start==end:
        tree[node]=val%MOD
        return
    mid=(start+end)//2
    update(start, mid, node * 2,idx,val)
    update(mid + 1, end, node * 2 + 1,idx,val)
    tree[node] = (tree[node*2]*tree[node*2+1]%MOD)
    return tree[node]

def query(start,end,node,left,right):
    if right<start or left>end:
        return 1
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    l_prod=query(start,mid,node*2,left,right)
    r_prod=query(mid+1,end,node*2+1,left,right)
    return (l_prod*r_prod)%MOD

init(1,n,1)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,n,1,b,c)
    else:
        print(query(1,n,1,b,c))
