import sys

input=sys.stdin.readline
n=int(input())

#아래부터 도착점까지
#각 계단에 쓰여 있는 점수, 마지막 도착 계단은 반드시 밟아야
#연속된 세 계단은 안됨, (시작점은 포함x)
dp=[0]*(n+1)
step=[0]



for _ in range(n):
    step.append(int(input()))
if n == 1:
    print(step[1])
    exit()
dp[1]=step[1]
dp[2]=step[1]+step[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-2]+step[i],dp[i-3]+step[i-1]+step[i])

print(dp[n])