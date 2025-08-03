import sys

input=sys.stdin.readline


n=int(input())
m=int(input())
graph=[[]for _ in range(n+1)]
dp=[[int(1e9)]*(n) for _ in range(n)]
for i in range(n):
    dp[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    dp[a][b]=min(dp[a][b],c)

for mid in range(n):
    for start in range(n):
        for end in range(n):
            dp[start][end]=min(dp[start][end],dp[start][mid]+dp[mid][end])

for i in range(n):
    for j in range(n):
        if dp[i][j]==int(1e9):
            print(0,end=' ')
        else:
            print(dp[i][j], end=' ')
    print('')
