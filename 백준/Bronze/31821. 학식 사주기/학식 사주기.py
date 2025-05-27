import sys

input=sys.stdin.readline
n=int(input())
menu=[int(input().strip()) for _ in range(n)]
m=int(input())
money=0

for _ in range(m):
    money+=menu[int(input())-1]
print(money)