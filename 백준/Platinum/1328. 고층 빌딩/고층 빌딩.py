import sys

input=sys.stdin.readline
n,l,r=map(int,input().split())
#dp [n][l][r]
dp=[[([0]*(r+1))for _ in range(l+1)]for _ in range(n+1)]
res=0

MOD=1000000007
dp[1][1][1]=1

for i in range(1, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            # 왼쪽에서 볼 수 있는 빌딩 증가
            if j>0:
                dp[i][j][k]+=dp[i-1][j-1][k]
            # 오른쪽에서 볼 수 있는 빌딩 증가
            if k>0:
                dp[i][j][k]+=dp[i-1][j][k-1]
            # 볼 수 있는 빌딩 개수 유지
            if i>2:
                dp[i][j][k]+=(i-2)*dp[i-1][j][k]

            dp[i][j][k]%=MOD

print(dp[n][l][r])