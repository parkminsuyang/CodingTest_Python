
import sys

input=sys.stdin.readline
n=int(input())
numbers=list(map(int, input().split()))

dp1=[0]*(n)
dp2=[0]*(n) #원소 하나 제거
dp1[0]=numbers[0]
dp2[0]=numbers[0]

if n==1:
    print(dp1[0])
    exit()

for i in range(1,n):
    dp1[i]=max(numbers[i], dp1[i-1]+numbers[i])
    dp2[i]=max(dp2[i-1]+numbers[i], dp1[i-1])

print(max(max(dp1), max(dp2)))