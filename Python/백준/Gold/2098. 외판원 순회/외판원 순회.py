import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

INF=int(1e9)
n=int(input())
cost=[]
dp=[[-1]*(1<<n) for _ in range(n)]

for _ in range(n):
    cost.append(list(map(int,input().split())))

def tsp(cur,visited):
    if visited==(1<<n)-1:
        if cost[cur][0]:
            return cost[cur][0]
        else:
            return INF
    if dp[cur][visited]!=-1:
        return dp[cur][visited]

    ans=INF
    for nxt in range(n):
        if not(visited&(1<<nxt)) and cost[cur][nxt]!=0:
            ans=min(ans,tsp(nxt,visited|(1<<nxt))+cost[cur][nxt])
    dp[cur][visited]=ans
    return ans
print(tsp(0,1))