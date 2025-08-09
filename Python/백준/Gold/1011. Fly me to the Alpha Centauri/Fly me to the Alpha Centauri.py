
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    x,y=map(int,input().split())
    dist = y - x
    n = 0
    while (n+1)**2 <= dist:
        n += 1
    if dist == n**2:
        print(2*n - 1)
    elif n**2 < dist <= n**2 + n:
        print(2*n)
    else:
        print(2*n + 1)