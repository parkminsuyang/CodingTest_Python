import sys
input=sys.stdin.readline
n=int(input())

def min_sticker(s,st):
    dp=[([0]*s) for _ in range(2)]
    dp[0][0] = st[0][0]
    dp[1][0] = st[1][0]
    if s==1:
        return dp
    dp[0][1] = st[0][1]+dp[1][0]
    dp[1][1] = st[1][1]+dp[0][0]
    if s>2:
        for i in range(2,s):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + st[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + st[1][i]
    return dp

for _ in range(n):
    a=int(input())
    sticker=[]
    for _ in range(2):
        sticker.append(list(map(int,input().split())))
    res=min_sticker(a, sticker)

    print(max(res[0][-1],res[1][-1]))