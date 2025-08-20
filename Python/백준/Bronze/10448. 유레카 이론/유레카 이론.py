import sys
from collections import deque

input = sys.stdin.readline

tri=[]
for i in range(1,50):
    tri.append((i*(i+1))//2)

tri_sum=set()
for i in tri:
    for j in tri:
        for k in tri:
            tri_sum.add(i+j+k)
t=int(input())

for _ in range(t):
    n=int(input())
    if n in tri_sum:
        print(1)
    else:
        print(0)

