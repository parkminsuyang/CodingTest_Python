import sys
from collections import Counter

input=sys.stdin.readline


n=int(input())
A=[]
B=[]
C=[]
D=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

res=0

AB=[ a+b for a in A for b in B]
CD=[ -(c+d) for c in C for d in D]
CD.sort()

cdCounter=Counter(CD)
for s in AB:
    res+=cdCounter[s]

print(res)