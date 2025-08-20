
import sys

input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

dp=[[[0]*(3) for _ in range(n)] for _ in range(n)]

dp[0][1][0]=1

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            continue

        if dp[i][j][0]:
            if (j+1)<n and board[i][j+1]==0:
                dp[i][j+1][0]+=dp[i][j][0]
                if i+1<n and board[i+1][j]==0 and board[i+1][j+1]==0:
                    dp[i+1][j+1][2]+=dp[i][j][0]

        if dp[i][j][1]:
            if i+1<n and board[i+1][j]==0:
                dp[i+1][j][1]+=dp[i][j][1]
                if j+1<n and board[i][j+1]==0 and board[i+1][j+1]==0:
                    dp[i+1][j+1][2]+=dp[i][j][1]


        if dp[i][j][2]:
            if j+1<n and board[i][j+1]==0 :
                dp[i][j+1][0]+=dp[i][j][2]
            if i+1<n and board[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][2]
                if j+1<n and board[i][j+1]==0 and board[i+1][j+1]==0:
                    dp[i+1][j+1][2]+=dp[i][j][2]


print(sum(dp[n-1][n-1]))