import sys
input=sys.stdin.readline
n=int(input())
MOD=1000000000

if n==1:
    print(0)
    exit()
dp=[0]*(n+1)
dp[1]=0
dp[2]=1
for i in range(3,n+1):
    dp[i]=((i-1)*(dp[i-1]+dp[i-2]))%MOD
print(dp[n])