import sys

input=sys.stdin.readline


n=int(input())
#자리수 끝자리숫자 비트마스크
dp=[[[0]*1024 for _ in range(10)] for _ in range(n+1)]

#첫 자리
for i in range(1,10):
    dp[1][i][1<<i]=1

#자리수
for j in range(2,n+1):
    #끝자리수
    for last in range(10):
        for bit in range(1024):
            if last>0:
                dp[j][last][bit | (1<<last)] += dp[j-1][last-1][bit]
                dp[j][last][bit | (1 << last)] %=1000000000
            if last<9:
                dp[j][last][bit | (1<<last)] += dp[j-1][last+1][bit]
                dp[j][last][bit | (1 << last)] %=1000000000

res=0
for i in range(10):
    res+=dp[n][i][1023]
    res%=1000000000
print(res)