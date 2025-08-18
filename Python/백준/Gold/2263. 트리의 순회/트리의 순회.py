import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
inorder=list(map(int,input().split())) #중위순회
postorder=list(map(int,input().split())) #후위순회

idx=[0]*(n+1)
for i,v in enumerate(inorder):
    idx[v]=i

def find(inorder_start,inorder_end,postorder_start,postorder_end):

    if inorder_start>inorder_end or postorder_start>postorder_end:
        return

    root=postorder[postorder_end]
    print(root, end=' ')

    root_idx=idx[root]
    left_size=root_idx-inorder_start

    find(inorder_start,root_idx-1,postorder_start,postorder_start+left_size-1)
    find(root_idx+1,inorder_end, postorder_start+left_size, postorder_end-1)


find(0,n-1,0,n-1)