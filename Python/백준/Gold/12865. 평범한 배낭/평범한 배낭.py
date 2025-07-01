import sys
input=sys.stdin.readline


n,k=map(int,input().split())

bag=[0]
for _ in range(n):
    w,k2=map(int,input().split())
    bag.append((w,k2))

dp=[[0]*(k+1) for _ in range(n+1)]
#dp[개수][무게]

for i in range(1,n+1):
    for j in range(1,k+1):

        if j<bag[i][0]:
            dp[i][j]=dp[i-1][j]

        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-bag[i][0]]+bag[i][1])

print(dp[n][k])