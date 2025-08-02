import sys

input=sys.stdin.readline

letter=list(input().strip())
n=len(letter)
pal=[[False]*n for _ in range(n)]
dp=[2500]*(n+1)
dp[-1]=0


for e in range(n):
    for s in range(e+1):
        if letter[s]==letter[e] and (e-s<2 or pal[s+1][e-1]):
            pal[s][e]=True
            dp[e]=min(dp[e],dp[s-1]+1)

print(dp[n-1])

