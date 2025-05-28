import sys

input=sys.stdin.readline
n,m=map(int,input().split())
number={}
for _ in range(n):
    site,pw=input().split()
    number[site]=pw
for _ in range(m):
    print(number[input().strip()])