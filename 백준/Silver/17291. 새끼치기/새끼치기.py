import sys

input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]*2
    if i==4:
        dp[i]-=1
        continue
    if i-3>0 and (i-3)%2==1:
        dp[i]-=dp[i-4]
    if i-4>0 and (i-4)%2==0:
        dp[i]-=dp[i-5]


print(dp[n])