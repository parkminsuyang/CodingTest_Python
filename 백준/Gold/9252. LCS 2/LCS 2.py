import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
lcs1=input().strip()
lcs2=input().strip()

n=len(lcs1)
m=len(lcs2)

dp=[[0]*(m+1) for _ in range (n+1)]
trace=[[0]*(m+1) for _ in range (n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if lcs1[i-1]==lcs2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            trace[i][j]='diag'
        elif dp[i][j - 1] >= dp[i - 1][j]:
            dp[i][j]=dp[i][j-1]
            trace[i][j]='left'
        else:
            trace[i][j]='up'
            dp[i][j]=dp[i-1][j]

print(dp[n][m])
if dp[n][m]==0:
    exit()
else:
    #역추적
    res=[]
    a,b=n,m
    while a>0 and b>0:
        if trace[a][b]=='diag':
            res.append(lcs1[a-1])
            a-=1
            b-=1
        elif trace[a][b]=='up':
            a-=1
        else:
            b-=1

    print(''.join(reversed(res)))

