import sys

input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))

long = [1] * n

for i in range(n):
    for j in range(i):
        if num[i]>num[j]:

            long[i]=max(long[i],long[j]+1)

print(max(long))
