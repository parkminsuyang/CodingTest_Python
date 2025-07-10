import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,r,q=map(int,input().split())
graph=[[] for _ in range(n+1)]
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def tree_making(cur,parent):
    for nxt in graph[cur]:
        if nxt!=parent:
            tree[cur].append(nxt)
            tree_making(nxt,cur)

tree_making(r,-1)

subtree=[0]*(n+1)

def subtree_counting(cur):
    subtree[cur]=1
    for sub in tree[cur]:
        subtree[cur]+=subtree_counting(sub)
    return subtree[cur]
subtree_counting(r)

for _ in range(q):
    U=int(input().strip())
    print(subtree[U])
