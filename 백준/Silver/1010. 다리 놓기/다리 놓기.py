import sys

input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    res=1
    for i in range(1,n+1):
        res=res*(m-i+1)//i
    print(res)