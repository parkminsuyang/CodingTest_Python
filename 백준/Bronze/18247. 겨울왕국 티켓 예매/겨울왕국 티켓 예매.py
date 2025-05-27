import sys

input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())

    if ord('L')-ord('A')+1<=n and m>=4:
        print((ord('L')-ord('A'))*m+4)
        
    else:
        print(-1)