import sys

input=sys.stdin.readline


n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(input().split()))

dp=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1':
            dp[i][j]=1

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if dp[start][mid] and dp[mid][end]:
                dp[start][end]=1

for i in range(n):
    print(' '.join(map(str,dp[i])))