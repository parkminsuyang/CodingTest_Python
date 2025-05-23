import sys
from bisect import bisect, bisect_left

input=sys.stdin.readline

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        exit()
    nlist=[]
    mlist=[]
    for _ in range(n):
        nlist.append(int(input()))
    for _ in range(m):
        mlist.append(int(input()))

    cnt=0

    if n<m:
        for i in nlist:
           exist=bisect_left(mlist,i)
           if exist<m and mlist[exist]==i:
               cnt+=1
    else:
        for j in mlist:
            exist=bisect_left(nlist,j)
            if exist<n and nlist[exist]==j:
                cnt+=1

    print(cnt)