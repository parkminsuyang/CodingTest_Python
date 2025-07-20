import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(cur):
    global res
    visited[cur]=True
    nxt=student[cur]

    if not visited[nxt]:
        dfs(nxt)
    elif not finished[nxt]:
        temp=nxt
        res+=1
        while temp!=cur:
            res+=1
            temp=student[temp]
    finished[cur]=True

t=int(input())

for _ in range(t):
    n=int(input())
    visited=[False]*(n+1)
    finished = [False] * (n + 1)
    student=[0]+list(map(int,input().strip().split()))
    res=0
    for i in range(1,n+1):
        dfs(i)
    print(n-res)


