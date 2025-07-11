import sys
input=sys.stdin.readline

n=int(input())
rgb=[0]
for _ in range(n):
    r,g,b=map(int,input().split())
    rgb.append((r,g,b))


ans=int(1e9)
for color in range(3):
    dp=[[int(1e9)]*(3) for _ in range(n+1)]
    dp[1][color]=rgb[1][color]


    for i in range(2,n+1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

    for last in range(3):
        if last==color:
            continue
        else:
            ans=min(ans,dp[n][last])
print(ans)