import sys

input=sys.stdin.readline


n,m=map(int,input().split())
dp=[[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    dp[a][b]=1
    dp[b][a]=1

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if dp[start][end]>dp[start][mid]+dp[mid][end]:
                dp[start][end] = dp[start][mid] + dp[mid][end]

min_value=int(1e9)
res=0
for i in range(1,n+1):
    total=sum(dp[i][1:])
    if total<min_value:
        min_value=total
        res=i
print(res)