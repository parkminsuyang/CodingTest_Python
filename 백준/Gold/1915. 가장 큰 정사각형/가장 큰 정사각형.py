
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
square=[list(input().strip()) for i in range(n)]
dp=[[0]*m for _ in range(n)]
res=0

for i in range(n):
    for j in range(m):
        if square[i][j]=='1':
            if i==0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

for i in range(n):
    res=max(res, max(dp[i]))

print(res**2)