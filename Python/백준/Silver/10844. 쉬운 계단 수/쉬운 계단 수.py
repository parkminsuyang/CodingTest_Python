import sys

input=sys.stdin.readline
n=int(input())
MOD=1000000000

dp=[[0]*10 for _ in range(n+1)] #dp[i][j]: 길이 i, 끝자리 j

for i in range(1,10):
    dp[1][i]=1

for i in range(1,n):
    for j in range(1,9):
        dp[i+1][j+1]+=dp[i][j]%MOD
        dp[i + 1][j - 1] += dp[i][j]%MOD
    dp[i+1][8]+=dp[i][9]%MOD
    if i>=2:
        dp[i+1][1]+=dp[i][0]%MOD

print(sum(dp[n])%MOD)