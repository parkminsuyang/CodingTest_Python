import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
dp=[[0,1] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,parent):
    for child in graph[node]:
        if parent==child:
            continue
        dfs(child,node)
        dp[node][0]+=dp[child][1]
        dp[node][1]+=min(dp[child][0],dp[child][1])

dfs(1,-1)
print(min(dp[1][0],dp[1][1]))