import sys
input=sys.stdin.readline
city=[]
c,n=map(int,input().split())
for _ in range(n):
    money,customer=map(int,input().split())
    city.append((money,customer))

dp=[int(1e9)]*(c+100)
dp[0]=0

for money,customer in city:
    for i in range(customer,len(dp)):
        dp[i]=min(dp[i-customer]+money,dp[i])

print(min(dp[c:]))