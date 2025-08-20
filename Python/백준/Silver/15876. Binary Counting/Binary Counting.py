import sys
from collections import deque

input = sys.stdin.readline

n,k=map(int,input().split())
res=""
for i in range(0,n*5):
    res+=(bin(i)[2:])

for j in range(k-1,n*5,n):
    print(res[j],end=" ")