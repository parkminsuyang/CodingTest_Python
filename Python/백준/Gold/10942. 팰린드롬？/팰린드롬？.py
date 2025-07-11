import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
num.insert(0,0)
m=int(input())
dp=[[0]*(n+1) for _ in range(n+1)]

#1개
for i in range(1,n+1):
    dp[i][i]=1
#2개
for i in range(1,n):
    if num[i]==num[i+1]:
        dp[i][i+1]=1
#3개 이상
for length in range(3,n+1):
    for start in range(1,n-length+2):
        end=start+length-1
        if num[start]==num[end] and dp[start+1][end-1]==1:
            dp[start][end]=1
        else:
            dp[start][end]=0

for _ in range (m):
    s,e=map(int,input().split())
    print(dp[s][e])