import sys

input=sys.stdin.readline
t=int(input())


wear={}
for _ in range(t):

    n=int(input())

    res=1
    wear={}
    
    for _ in range(n):
        a,b=input().split()
        if b not in wear:
            wear[b]=[]
        wear[b].append(a)
    for k in wear:
        res*=(len(wear[k])+1)
    print(res-1)
