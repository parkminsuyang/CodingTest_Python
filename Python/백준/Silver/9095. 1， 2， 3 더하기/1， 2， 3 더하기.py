import sys

input=sys.stdin.readline
n=int(input())

#정수 n이 주어졌을때 n을 1,2,3의 합으로 나타내는 방법의 수 구하기
for _ in range(n):


    t=int(input())
    dp=[0]*(t+1)
    dp[0]=1
    for i in range(1,t+1):
        if i-1>=0:
            dp[i]+=dp[i-1]
        if i-2>=0:
            dp[i]+=dp[i-2]
        if i-3>=0:
            dp[i]+=dp[i-3]
    print(dp[t])
