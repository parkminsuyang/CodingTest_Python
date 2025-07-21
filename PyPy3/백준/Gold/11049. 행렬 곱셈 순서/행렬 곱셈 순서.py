import sys
input=sys.stdin.readline
n=int(input())
graph=[]
dp=[[int(1e9)]*(n) for _ in range(n) ]

for _ in range(n):
    r,c=map(int,input().split())
    graph.append((r,c))

for i in range(n):
    dp[i][i]=0

for length in range(2,n+1):
    for start in range(n-length+1):
        end=start+length-1
        for mid in range(start,end):
            dp[start][end]=min(dp[start][end],dp[start][mid]+dp[mid+1][end]+graph[start][0]*graph[mid][1]*graph[end][1])



print(dp[0][n-1])