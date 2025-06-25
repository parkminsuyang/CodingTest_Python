import sys
input=sys.stdin.readline

a=int(input())

color=[]

for i in range(a):
    r,g,b=map(int,input().split())
    color.append([r,g,b])

dp=[[] for _ in range(a)]
dp[0]=color[0]

for i in range(1,a):
    dp[i].append(min(dp[i-1][1],dp[i-1][2])+color[i][0])
    dp[i].append(min(dp[i - 1][0], dp[i - 1][2]) + color[i][1])
    dp[i].append(min(dp[i - 1][1], dp[i - 1][0]) + color[i][2])

print(min(dp[a-1]))